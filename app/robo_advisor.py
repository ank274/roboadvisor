from dotenv import load_dotenv
import os
import requests

load_dotenv()

key = os.environ.get("ALPHAVANTAGE_API_KEY")

data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MFST&apikey={}'.format(key))
data = data.json()
print(data)