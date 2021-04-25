import os
import requests

cd = os.path.dirname(os.path.realpath(__file__))
apikeypath = cd + "/apikey.txt"

apikeyfile = open(apikeypath)
apikey = apikeyfile.readline()[0:-1]
print(apikey)
