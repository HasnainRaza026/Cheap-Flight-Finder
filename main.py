from flight_data import FlightData
from flight_search import FlightSearch
from send_sms import SMSNotifier

class Flights:
    def __init__(self):
        self.data_manager = FlightData()
        self.flight_searcher = FlightSearch()
        self.notifier = SMSNotifier()

    def run(self):
        data = self.data_manager.get_data()
        cheap_flights = self.flight_searcher.search_for_deals(data)
        if cheap_flights:
            self.notifier.send_alerts(cheap_flights)

if __name__ == '__main__':
    flight = Flights()
    flight.run()
