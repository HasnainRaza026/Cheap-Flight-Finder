import unittest
from unittest.mock import patch
from flight_search import FlightSearch

class TestFlightSearch(unittest.TestCase):

    @patch('amadeus.Client.shopping.flight_offers_search.get')
    def test_search_for_deals(self, mock_search):
        mock_search.return_value.data = [{
            "price": {"grandTotal": "45.00"}
        }]
        flight_search = FlightSearch()
        destinations = [("Paris", "PAR", 50)]
        cheap_flights = flight_search.search_for_deals(destinations)
        expected_flights = [("Paris", "PAR", unittest.mock.ANY, 45.0)]
        self.assertEqual(cheap_flights, expected_flights)

if __name__ == '__main__':
    unittest.main()
