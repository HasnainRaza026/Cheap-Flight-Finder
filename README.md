# **Cheap Flight Finder**

## **Table of Contents**
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## **Project Overview**

**Cheap Flight Finder** is an automated Python-based application that helps users find and get notified about the cheapest flights available from a specified departure city to various destinations. The program fetches flight prices using the Amadeus API, compares them with user-defined thresholds, and sends alerts via SMS using Twilio when a flight deal is found.

## **Features**

- **Automated Flight Search:** Searches for flight deals from a specified departure city to various destinations over the next 6 months.
- **Customizable Alerts:** Sends SMS notifications to users when a cheap flight is found.
- **Easy Configuration:** Easily configurable via environment variables for API keys, city codes, and phone numbers.
- **Modular Design:** The project is designed in a modular way, making it easy to extend or modify.

## **Technologies Used**

- **Python 3.x**
- **Amadeus API** for flight search
- **Sheety API** for managing destination data
- **Twilio API** for SMS notifications
- **dotenv** for managing environment variables
- **unittest** for testing

## **Project Structure**

```bash
├── flight_data.py        # Handles data fetching from the Google Sheet using the Sheety API
├── flight_search.py      # Manages flight search using the Amadeus API
├── send_sms.py           # Sends SMS alerts using the Twilio API
├── main.py               # Main entry point of the application
├── Unit Test/test_flight_data.py   # Unit tests for flight_data.py
├── Unit Test/test_flight_search.py # Unit tests for flight_search.py
├── .env                  # Environment variables file (not included in the repository)
└── README.md             # Project documentation
```



## **Setup and Installation**

### Prerequisites

- Python 3.x installed on your machine.
- Accounts with [Amadeus API](https://developers.amadeus.com/) and [Twilio](https://www.twilio.com/).
- A Google Sheet set up and connected via [Sheety API](https://sheety.co/).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cheap-flight-finder.git
   cd cheap-flight-finder
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required Python packages:**
   ```bash
    pip install -r requirements.txt
    ```

4. **Create a .env file:**

   Create a .env file in the project root directory with the required environment variables (see below).


## **Environment Variables**
The following environment variables need to be set in a .env file:
```
SHEETY_URL="https://api.sheety.co/your_endpoint"
SHEETY_API_KEY="your_api_key"
FLIGHT_API_KEY="your_flight_api_key"
FLIGHT_API_SECRETE="your_flight_api_secret"
ACCOUNT_SID="your_twilio_sid"
AUTH_TOKEN="your_twilio_auth_token"
FROM_NO="+123456789"
TO_NO="+987654321"
```

- SHEETY_URL: The URL of your Sheety API endpoint.
- SHEETY_API_KEY: The API key for Sheety.
- FLIGHT_API_KEY: The API key for the Amadeus API.
- FLIGHT_API_SECRETE: The secret for the Amadeus API.
- ACCOUNT_SID: Your Twilio account SID.
- AUTH_TOKEN: Your Twilio authentication token.
- FROM_NO: The Twilio phone number sending the SMS.
- TO_NO: The recipient's phone number.


## **Usage**
To run the application:

1. Ensure that your .env file is correctly set up with all the required environment variables.

2. Run the main.py script:

```bash
python main.py
```
This will:

- Fetch the destination data from the Google Sheet.
- Search for flight deals using the Amadeus API.
- Send SMS alerts for any deals found.

## **Testing**
Unit tests are provided for the core functionalities of the application.

To run the tests:


```bash
python -m unittest discover
```
This will execute all the test cases in the project.