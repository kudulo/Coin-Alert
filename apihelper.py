import requests
import filehelper
import smtplib, datetime
from email.message import EmailMessage

email = "your_Email"
passwd = "hashed password"
phoneNum = "Your_Phone#"


apikey = filehelper.open_file_cd("apikey.txt").readline()
apiurl = "https://api.coingecko.com/api/v3"
apiheaders = {"Authorization": "Bearer " + apikey}
id = "dogecoin"
price = 0.6
price_low = 0.54

####################################################################################################################################################################################################

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
    url = "currencies/ticker?key=" + apikey + "&ids=" + id + "&interval=1h&per-page=100&page=1"
    return request(url)

#####################################################################################################################################################################################################

while True:

    url = "/coins/" +id+ "?localization=en&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false"

    pr = request(url).json()

    pr = pr["market_data"]["current_price"]["usd"]
    print(pr)

#####################################################################################################################################################################################################


    def email_alert(body, to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['to'] = to

        user = email
        password = passwd

        msg['from'] = user

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
        server.quit()


#####################################################################################################################################################################################################

    if pr >= price:
        price = price * 1.2
        email_alert(id + " is at " + str(pr), phoneNum + "@vtext.com")
        print(price)
    elif pr <= price_low:
        price_low = price_low * .9
        email_alert(id + " is at " + str(pr), phoneNum + "@vtext.com")
        print(price_low)
