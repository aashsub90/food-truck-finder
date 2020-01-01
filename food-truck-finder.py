#!/usr/bin/env python3
import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError, TooManyRedirects, RequestException
from datetime import datetime
from pytz import timezone
import argparse
import json
import os
import logging
from tabulate import tabulate
import config

LOG_PATH = os.environ["LOG_PATH"]
logging.basicConfig(filename=LOG_PATH+"food_trucks.log", filemode="a", format="%(asctime)s - %(name)s - [%(threadName)s] - [%(levelname)s] - %(message)s", level=logging.INFO)
log = logging.getLogger(__name__)

class FoodSource(object):
    def __init__(self, date_time):
        # Initialize the timestamp and source url
        self.timestamp = date_time
        self.api_url = config.get_config('API', 'trucks_api_url')

    def get_data(self, offset):
        """Get the filtered data using the API
        
        Arguments:
            offset {integer} -- Offset value for pagination control
        
        Returns:
            List -- List of JSON objects containing valid food sources
        """
        open_trucks_data = None

        # Extract query parameters
        day_of_week = self.timestamp.strftime('%A') 
        time = self.timestamp.strftime('%H:%M')

        log.info("Fetching data with offset {}".format(offset))
        # Generate url
        url = self.api_url+"$query=SELECT applicant as Name, \
            location as Address WHERE dayofweekstr='{day_of_week}' AND '{time}' BETWEEN start24 AND end24 \
            ORDER BY applicant LIMIT 10 OFFSET {offset}".format(day_of_week=day_of_week, time=time, offset=offset)
        try:
            open_trucks_data = requests.get(url, timeout=5).json() # Fetch the data using API
        except HTTPError as e:
            log.error(e)
        except Timeout as e:
            log.error(e)
        except ConnectionError as e:
            log.error(e)
        except TooManyRedirects as e:
            log.error(e)
        except RequestException as e:
            log.error(e)
        return open_trucks_data

    def display_data(self, data):
        """Display the name and address of the food source 
        
        Arguments:
            data {json} -- List of JSON objects containing the name and address 
        """
        log.info("Data retreived: {}".format(data))
        print(tabulate(data, headers="keys", tablefmt="simple"))

    def fetch(self):
        """Fetch data and display the list of food sources available
        """
        offset = 0 # Initialize offset to start at first record
        print("\nFood trucks open in San Francisco at {timestamp}:\n".format(timestamp=self.timestamp.strftime("%H:%M %Y-%m-%d")))
        while True:
            # Get the open food truck data
            data = self.get_data(offset)
            if not data:
                print("\nNo more open food trucks were found.\n") # Break on end of list
                break
            self.display_data(data)
            # Wait for the user to request for more data
            user_response = input("\nHit 'N' or 'n' to receive more results: ") 
            if user_response.lower() != "n":
                log.info("User Exited with command: {}".format(user_response))
                break
            offset+=10
        log.info("Data fetch complete")

def main(current_timestamp):
    log.info("Food Truck data fetched for timestamp - {}".format(current_timestamp))
    # Create instance of FoodSource class
    data_fetcher = FoodSource(current_timestamp)
    data_fetcher.fetch()

if __name__ == "__main__":
    # Get current time in SF
    current_timestamp = datetime.now(timezone('UTC')).astimezone(timezone('America/Los_Angeles'))

    # Accept user input if any or assign default
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", "-d", help="Date formatted in YYYY-MM-DD (e.g. 2019-12-31) [default to current date]", default=current_timestamp.strftime("%Y-%m-%d"))
    parser.add_argument("--time", "-t", help="Time in 24 hour format - H:M (e.g. 23:15) [default to current time]", default=current_timestamp.strftime("%H:%M"))
    args = parser.parse_args()
    timestamp = datetime.strptime(args.date+" "+args.time, '%Y-%m-%d %H:%M')
    main(timestamp)