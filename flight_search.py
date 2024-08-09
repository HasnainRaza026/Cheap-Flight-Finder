import logging
import os
from dotenv import find_dotenv, load_dotenv
from amadeus import Client, ResponseError
from datetime import datetime, timedelta
import time
import random

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlightSearch:
    """
        Class to search for flight deals using the Amadeus API.

        Attributes:
            departure_city (str): The IATA code of the departure city.

        Methods:
            search_for_deals(destinations): Searches for flight deals to the specified destinations.
        """
    def __init__(self, departure_city="KHI"):
        # Load environment variables
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.amadeus = Client(
            client_id=os.getenv("FLIGHT_API_KEY"),
            client_secret=os.getenv("FLIGHT_API_SECRETE")
        )
        self.departure_city = departure_city

    def search_for_deals(self, destinations):
        """Searches for flight deals for the given destinations.

                Args:
                    destinations (list): A list of destination tuples (city, IATA code, lowest price).

                Returns:
                    list: A list of tuples containing destination city, IATA code, departure date, and price.
                """
        cheapest_flight = []
        try:
            for destination in destinations:
                cheapest_price = destination[2]
                for month_offset in range(6):  # Next 6 months
                    departure_date = (datetime.now() + timedelta(days=month_offset * 30)).strftime("%Y-%m-%d")
                    response = self.amadeus.shopping.flight_offers_search.get(
                        originLocationCode=self.departure_city,
                        destinationLocationCode=destination[1],
                        departureDate=departure_date,
                        adults=1
                    )
                    flights = response.data
                    if flights:
                        flight_price = float(flights[0]["price"]["grandTotal"])
                        if flight_price <= cheapest_price:
                            cheapest_flight.append((destination[0], destination[1], departure_date, flight_price))
                    time.sleep(random.uniform(1, 3))  # Random sleep to avoid hitting API rate limits
            return cheapest_flight
        except ResponseError as error:
            logger.error(f"API request error: {error}")
            return None
