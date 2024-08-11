##  Gate.io Futures Trades Table - Flask Application

This project demonstrates a Flask application that retrieves your recent Gate.io futures trades and displays them in an HTML table.

### Project Structure

The project contains the following files and folders:

* **`app.py`:** The main Flask application code.
* **`api.py`:**  Handles API interactions with the Gate.io API to retrieve trade data.
* **`authm/auth.py`:**  Handles loading API credentials from a YAML file.
* **`templates/trades_table.html`:**  The HTML template for displaying the trades table.

### Functionality

1. **API Integration:** The `api.py` module utilizes the `gate_api` library to authenticate with the Gate.io API and retrieve your recent futures trades.
2. **Credentials Loading:** The `authm/auth.py` module loads API credentials securely from a YAML file (auth/auth.yml). You need to provide your API key and secret in this file.
3. **Flask App:** The `app.py` file sets up the Flask app, defines the route (`/`) for the trades table, and renders the HTML template (`trades_table.html`).
4. **HTML Table Rendering:**  The `trades_table.html` template dynamically displays the fetched trade data in a formatted table.

### Prerequisites

* **Python 3.6 or higher:** Install Python if you don't have it already.
* **Flask:** Install Flask using `pip install Flask`.
* **gate_api:** Install the Gate.io API library using `pip install gate_api`.
* **PyYAML:** Install the PyYAML library for loading credentials from the YAML file using `pip install PyYAML`.

### Setup

1. **Create a Gate.io API Key and Secret:**
    * Go to your Gate.io account settings and create a new API key with necessary permissions.
2. **Store API Credentials:**
    * Create a file named `auth/auth.yml` in the project root directory and add your API key and secret:
    ```yaml
    key: YOUR_API_KEY
    secret: YOUR_API_SECRET
    ```
3. **Install Dependencies:**
    * Install the required Python packages using the command: `pip install -r requirements.txt`
4. **Run the Application:**
    * Run the Flask application using `python app.py`. This will start the server, and you can access the trades table at `http://127.0.0.1:5000/`.

### Important Notes

* **Security:**  Store your API credentials securely. Consider using environment variables or a dedicated secrets management solution instead of storing them directly in the `auth.yml` file.
* **API Rate Limits:**  Be aware of the Gate.io API rate limits. Avoid making excessive requests in a short period to prevent rate limiting.

### Further Development

* **Additional Data:**  Extend the application to retrieve and display other data, such as order history, account balance, or market information.
* **Interactive Features:**  Add interactivity to the table, allowing users to filter, sort, or download the data.
* **Error Handling:**  Implement robust error handling to gracefully handle cases like API errors or invalid credentials.
* **Security Enhancements:**  Implement authentication and authorization to control access to the application.

This README provides a basic overview of the project. Further documentation for specific functionalities or additional features can be added as needed.


