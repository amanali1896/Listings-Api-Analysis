#install "requests" using pip install requests
#install "JSON" using pip install json
#This displays all active cryptocurrency listings in one call

import json
import requests

listing_url = 'https://api.coinmarketcap.com/v2/listings/'#the url of the api

request = requests.get(listing_url)#this fetches the URL and returns the data in JSON format, assigning it to 'request' variable
results = request.json() ##converts the variable to a json format, and that is how we expect the results to be shown.

print(json.dumps(results, sort_keys=True, indent=4))
#.dumps converts the result to a string. sort_keys is made true so that the keys are coming in a sorted order
#indent is made equal to 4 spaces because it prints it in an indented format

data = results['data'] #sends data attribute from json to data variable

for currency in data: # we loop through all the attributes in list and then print out the data as per the format
    rank = currency['id'] #storing the data in the variable
    name = currency['name']
    symbol = currency['symbol']
    print(str(rank) + ': ' + name + ' (' + symbol + ')') #formatting the output
