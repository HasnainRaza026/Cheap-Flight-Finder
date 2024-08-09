import time
import logging
import os
from twilio.rest import Client
from dotenv import find_dotenv, load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SMSNotifier:
    def __init__(self):
        # Load environment variables
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))
        self.from_no = os.getenv("FROM_NO")
        self.to_no = os.getenv("TO_NO")

    def send_alerts(self, cheap_flights):
        for flight in cheap_flights:
            msg = f"Low price alert! Only €{flight[3]} to fly from Karachi (KHI) to {flight[0]} ({flight[1]}) on {flight[2]}."
            try:
                message = self.client.messages.create(
                    body=msg,
                    from_=self.from_no,
                    to=self.to_no
                )
                logger.info(f"Message sent with status: {message.status}")
            except Exception as e:
                logger.error(f"Failed to send SMS: {e}")
            time.sleep(5)
