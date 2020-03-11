import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Obtain the URL of the Veja shoes
URL = 'https://www.veja-store.com/en/women/2913-v-12-leather-extra-white-guimauve-marsala.html'

# My user agent
headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

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

    server.login('eganconor759@gmail.com', 'bzmemnkghqexesjv')

    subject = 'The Veja shoes are within your budget!'
    body = 'The V-12 WHITE GUIMAUVE MARSALA are in your price range. Check the link to the veja website to get Graces birthday present: https://www.veja-store.com/en/women/2913-v-12-leather-extra-white-guimauve-marsala.html'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'eganconor759@gmail.com',
        's1980812@ed.ac.uk',
        msg
    )
    print("HEY EMAIL HAS BEEN SENT!")

    server.quit()


# Check the price daily
while(True):
    check_price()
    time.sleep(60 * 60 * 24)
