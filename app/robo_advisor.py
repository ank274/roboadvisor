from dotenv import load_dotenv
import os
import requests
import pandas as pd
import datetime

choice = ""
reason = ""
date = datetime.datetime.now()

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
    csv_read = pd.read_csv("../data/price_{}.csv".format(user_input))
    median = float(csv_read['low'].median())
    high = float(csv_read['high'].max())
    current = csv_read.iloc[0]["close"]
    print("Selected Stock " + user_input)
    print("Date Runned:{} Time {}".format(date.strftime("%x"),date.strftime('%X')))
    print("Last Refreshed " + parsed_data['Meta Data']['3. Last Refreshed'])
    print("high $" + str(round(float(parsed_data['Time Series (Daily)'][all_date[0]]['2. high']),2)))
    print("low $" + str(round(float(parsed_data['Time Series (Daily)'][all_date[0]]['3. low']),2)))
    print("close $" + str(round(float(parsed_data['Time Series (Daily)'][all_date[0]]['4. close']),2)))
    if(current <= median):
        response = "buy"
        reason = "It is equal to or lower than the median of all the low values for the last 100 days"
    elif(current >= high):
        repsone ="do not buy"
        reason = "It is equal to or higher than the highest value of the last 100 das=ys"
    else:
        reason = "It is greater than the median of the lowest values of the last 100 days"
        response="Do not buy"
    print("RECOMMENDATION: {}".format(response))
    print("Reason {}".format(reason))
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")



