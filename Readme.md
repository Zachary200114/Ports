# Simple Port Scanner Web Application

This repository contains a simple web application for scanning open ports on a target IP address or domain. It uses Flask for the web interface and Python's `socket` library for port scanning.

## **Features**

- **Web-based Interface:** Easy-to-use interface for entering target IP/domain.
- **Concurrent Scanning:** Utilizes `ThreadPoolExecutor` for faster port scanning.
- **Clear Results:** Displays open ports in a user-friendly format.
- **Error Handling:** Provides error messages for invalid input.
- **Time limited scanning:** Stops the scan after 5 seconds to prevent excessive scan times on the system.

## **Prerequisites**

- Python 3.6+
- Flask (`pip install Flask`)

## **Installation**

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/port-scanner.git](https://github.com/your-username/port-scanner.git)
    cd port-scanner
    ```

2.  **Install Flask:**

    ```bash
    pip install Flask
    ```

## **Usage**

1.  **Run the Flask application:**

    ```bash
    python port-scanner.py
    ```

2.  **Open your web browser and navigate to:**

    ```
    [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
    ```

3.  **Enter the target IP address or domain in the input field and click "Scan".**

4.  **View the scan results displayed on the page.**

## **Code Explanation**

- **`index.html`:**
  -      Provides the HTML structure for the web interface.
  -      Includes a form for entering the target IP/domain.
  -      Uses Jinja2 templating to display scan results and error messages.
- **`port-scanner.py`:**
  -      Uses Flask to create a web application.
  - `scan_port(target, port)` function: Attempts to connect to a specific port on the target.
  - `/` route: Renders the main page.
  - `/scan` route: Handles the form submission, performs the port scan using `ThreadPoolExecutor`, and renders the results.
  - Uses a 5 second timer to limit the amount of scanned ports.
  - Handles exceptions during the port scanning process.

## **ThreadPoolExecutor usage explanation**

The `ThreadPoolExecutor` is utilized to improve the speed of the port scanning process. Instead of sequentially checking each port, it creates a pool of worker threads that can concurrently scan multiple ports. This dramatically reduces the overall scan time.

The code submits each port scan as a separate task to the executor. The `futures` list stores the results of these tasks. Once all tasks are submitted, the code iterates through the `futures` list, retrieves the results, and displays the open ports.

The timeout in the `future.result(timeout=1)` line is used to prevent the script from hanging if a particular port scan takes too long.

## **Limitations**

- This is a basic port scanner and may not detect all open ports in complex network environments.
- The speed of the scan depends on network conditions and the target host.
- The scan is limited to the first 5 seconds of ports.
- This tool should only be used on systems you have explicit permission to scan. Unauthorized port scanning is illegal.
- This script does not handle UDP ports.
