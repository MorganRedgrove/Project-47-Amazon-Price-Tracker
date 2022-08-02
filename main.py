import requests
from bs4 import BeautifulSoup
import pprint
import smtplib

pp= pprint.PrettyPrinter()

headers = {
"Accept-Language": "en-GB,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
}

response = requests.get(url="https://www.amazon.co.uk/Logitech-G502-Wireless-Programmable-Next-Generation/dp/B07QKC4WWD?th=1", headers=headers)
string = response.text
soup = BeautifulSoup(string, features="html.parser")
price = soup.find(name="span", class_="a-offscreen").getText()
print(price)

price_split = price.split("£", 1)
price_flt = float(price_split[1])

if price_flt <= 80.00:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user="", password="")
    connection.sendmail(from_addr="",
                        to_addrs="",
                        msg=f"Subject:G502 Price Drop\n\nThe Logitech G502 has dropped in price to £{price_flt}.")
    connection.close()