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
parsed_data = data.json()
if ('Error Message' in parsed_data or response !=200):
     print("error not a valid stock")
     exit()
else:
    all_date = list(parsed_data['Time Series (Daily)'])
    file_name = "../data/price_{}.csv".format(user_input)
    f = open(file_name, "w")
    headers = "date,open,high,low,close,volume\n"
    f.write(headers)
    for date_list in all_date:
        f.write(date_list + "," + parsed_data['Time Series (Daily)'][date_list]["1. open"] + "," 
        + parsed_data['Time Series (Daily)'][date_list]["2. high"] + "," + parsed_data['Time Series (Daily)'][date_list]["3. low"] 
        + "," + parsed_data['Time Series (Daily)'][date_list]["4. close"] + "," + parsed_data['Time Series (Daily)'][date_list]["5. volume"] + "\n")
    f.close()


