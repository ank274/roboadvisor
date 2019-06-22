from dotenv import load_dotenv
import os
import requests

load_dotenv()

key = os.environ.get("ALPHAVANTAGE_API_KEY")

user_input = input("Please enter a Stock symbol")
length = len(user_input)
if (length <= 0 or length > 6):
    print("inncorrect length")
    exit()
elif(user_input.isdigit()):
    print("Input cannot be a digit")
    exit()
data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(user_input,key))
response = data.status_code
parse_data = data.json()
if ('Error Message' in data.text or response !=200):
     print("error not a valid stock")
     exit()

