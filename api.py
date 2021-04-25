import os
import requests

# reading in the api key from the apikey.txt in the directory with this file
cd = os.path.dirname(os.path.realpath(__file__))
apikeypath = cd + "/apikey.txt"
apikeyfile = open(apikeypath)
apikey = apikeyfile.readline()[0:-1]

# api functions
apiurl = "https://api.bscscan.com/api?module="


def request(url):
    response = requests.get(apiurl + url)
    if response.status_code != 200:
        print("Error", response.status_code, response.json())
    return response


def post(url, data):
    response = requests.post(apiurl + url, data=data)
    if response.status_code != 200:
        print("Error", response.status_code, response.json())
    return response
