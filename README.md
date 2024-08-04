# Whois Lookup Tool

A simple command-line tool for querying WHOIS information using Python. This project allows you to retrieve and display domain registration details such as the registrant's name, contact information, and registration dates.

## Features

- Retrieve WHOIS information for a given domain.
- Display domain registration details in a structured format.
- Save WHOIS data to a local SQLite database.

## Requirements

- Python 3.10 or higher
- `Flask==2.2.3`
- `requests==2.28.2`
- `beautifulsoup4==4.12.0`
- `SQLAlchemy==2.0.12`
- `redis==4.5.3`
- `Werkzeug>=2.2.2`
- `itsdangerous>=2.0`
- `Jinja2>=3.0`
- `click>=8.0`
- `urllib3<1.27,>=1.21.1`
- `charset-normalizer<4,>=2`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Alturnaks/whois.git
    ```

2. Navigate to the project directory:

    ```bash
    cd whois
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - **Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **Mac/Linux:**

      ```bash
      source venv/bin/activate
      ```

5. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Follow the prompts to enter a domain name and retrieve WHOIS information.

## Database

The project includes a SQLite database (`whois_data.db`) to store WHOIS data. The database is located in the `/app` directory.

## Docker

To build and run the application using Docker, use the following commands:

1. Build the Docker image:

    ```bash
    docker build -t whois-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 whois-app
    ```


