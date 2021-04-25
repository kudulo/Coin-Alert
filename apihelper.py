import requests
import filehelper

apikey = filehelper.open_file_cd("apikey.txt").readline()
apiurl = "https://api.bscscan.com/api?module="
apiheaders = {"Authorization": "Bearer " + apikey}


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


print(request("token&action=tokeninfo&contractaddress=0xd1587ee50e0333f0c4adcf261379a61b1486c5d2&apikey=" + apikey).json())
