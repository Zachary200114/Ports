from flask import Flask, request, render_template
import socket
import time
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

def scan_port(target, port):
    """
    Attempt to connect to the specified target and port.
    Returns a tuple (port, True) if the port is open; otherwise (port, False).
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        s.close()
        return port, (result == 0)
    except Exception:
        return port, False

@app.route('/')
def index():
    # Render the main page with the search bar.
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    # Retrieve the target from the form.
    target = request.form.get('target')
    if not target:
        return render_template('index.html', error="Please enter a target host.")

    open_ports = []
    start_time = time.time()

    # Use ThreadPoolExecutor for concurrent port scanning.
    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = []
        # Scan ports 1 to 65535, but stop submitting new tasks after 5 seconds.
        for port in range(1, 65536):
            if time.time() - start_time > 5:
                break
            futures.append(executor.submit(scan_port, target, port))
        # Process the results as they complete.
        for future in futures:
            try:
                port, is_open = future.result(timeout=1)
                if is_open:
                    open_ports.append(port)
            except Exception:
                continue

    # Render the page again with the results.
    return render_template('index.html', target=target, open_ports=open_ports)

if __name__ == '__main__':
    # Run the Flask app in debug mode.
    app.run(debug=True)
