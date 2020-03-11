import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Obtain the URL of the Veja shoes
URL = 'https://www.veja-store.com/en/women/2913-v-12-leather-extra-white-guimauve-marsala.html'

# My user agent
headers = {
    "User-Agent": ''}

# Create a function that checks the price of the Veja shoes


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="our_price_display").get_text()

    converted_price = float(price[0:3])

    if (converted_price < 100):
        send_mail()

    print(converted_price)

# Create a function to send an email alert
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# Insert email as first argument and two step password as second argument
    server.login('', '')

    subject = 'The Veja shoes are within your budget!'
    body = 'The V-12 WHITE GUIMAUVE MARSALA are in your price range. Check the link to the veja website to get Sarahs birthday present: https://www.veja-store.com/en/women/2913-v-12-leather-extra-white-guimauve-marsala.html'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
#First argument is the sender of the email and the second argument is the receipient of the email 
        '',
        '',
        msg
    )
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()


# Check the price daily
while(True):
    check_price()
    time.sleep(60 * 60 * 24)
