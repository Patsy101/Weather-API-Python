import requests
from dotenv import load_dotenv
import os
from pprint import pprint
# pretty print json
load_dotenv()

def get_current_weather():
    print('\n*** Get Current Weather Conditions ***\n')
    
    city = input("\nPlease enter a city name:\n")
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}units=metric'
    
    pprint(request_url)

if __name__ == "__main__": 
    get_current_weather()