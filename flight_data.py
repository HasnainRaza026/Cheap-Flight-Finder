import requests
import logging
import os
from dotenv import find_dotenv, load_dotenv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FlightData:
    """
        Class to manage flight data from a Google Sheet via the Sheety API.

        Methods:
            get_data(): Fetches data from the Google Sheet.
        """

    def __init__(self):
        # Load environment variables
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.sheety_url = os.getenv("SHEETY_URL")
        self.sheety_api_key = os.getenv("SHEETY_API_KEY")

    def get_data(self):
        """Fetches data from the Google Sheet using the Sheety API.

                Returns:
                    list: A list of tuples containing city, IATA code, and lowest price.
                """
        sheety_headers = {
            "Authorization": f"Bearer {self.sheety_api_key}",
            "Content-Type": "application/json"
        }
        try:
            response = requests.get(self.sheety_url, headers=sheety_headers)
            response.raise_for_status()
            data = [(i["city"], i["iataCode"], i["lowestPrice"])
                    for i in response.json()["sheet1"]]
            logger.info(f"Data fetched successfully: {data}")
            return data
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error occurred: {http_err}")
        except Exception as err:
            logger.error(f"An error occurred: {err}")
        return []
