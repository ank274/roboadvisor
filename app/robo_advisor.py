from dotenv import load_dotenv
import os
import requests

load_dotenv()

key = os.environ.get("ALPHAVANTAGE_API_KEY")

data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MFST&apikey={}'.format(key))
data = data.json()


user_input = input("Please enter a Stock symbol")
length = len(user_input)
if (length <= 0 or length > 6):
    print("inncorrect length")
    exit()
elif(user_input.isdigit()):
    print("Input cannot be a digit")
    exit()