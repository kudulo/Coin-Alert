import requests
import filehelper

apikey = filehelper.open_file_cd("apikey.txt").readline()
apiurl = "https://api.nomics.com/v1"
apiheaders = {"Authorization": "Bearer " + apikey}
ids = "WINDY"


def request(url):
    response = requests.get(apiurl + url, headers=apiheaders)
    if response.status_code != 200:
        print("Error", response.status_code, response.json())
    return response


def post(url, data):
    response = requests.post(apiurl + url, data=data, headers=apiheaders)
    if response.status_code != 200:
        print("Error", response.status_code, response.json())
    return response

def currency(ids):
    url = "currencies/ticker?key=" + apikey + "&ids=" + ids + "&interval=1h&per-page=100&page=1"
    return request(url)



response = request("/currencies/ticker")

import urllib.request
url = "https://api.nomics.com/v1/currencies/ticker?key="+ apikey + "&ids=BTC&interval=1d&convert=USD&per-page=1&page=1"
print(urllib.request.urlopen(url).read())
