import unittest
from unittest.mock import patch
from flight_data import FlightData


class TestFlightData(unittest.TestCase):

    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "sheet1": [
                {"city": "Paris", "iataCode": "PAR", "lowestPrice": 50},
                {"city": "Berlin", "iataCode": "BER", "lowestPrice": 60},
            ]
        }
        flight_data = FlightData()
        data = flight_data.get_data()
        expected_data = [("Paris", "PAR", 50), ("Berlin", "BER", 60)]
        self.assertEqual(data, expected_data)

    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        mock_get.side_effect = Exception("API error")
        flight_data = FlightData()
        data = flight_data.get_data()
        self.assertEqual(data, [])


if __name__ == '__main__':
    unittest.main()
