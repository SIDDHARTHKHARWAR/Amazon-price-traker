import requests
from bs4 import BeautifulSoup as BS
from smtplib import SMTP
url = "https://www.google.com/finance/quote/AMZN:NASDAQ"
def extract_price():
    page = requests.get(url)
    soup = BS(page.content, "html.parser")
    price = float(soup.find(class_="YMlKec fxKbKc").text.replace("$", "").replace(",", ""))
    return price
SMTP_SERVER = "smtp.gmail.com"
PORT = 587
EMAIL_ID = "196301039@gkv.ac.in"
PASSWORD = "Gujjar@9837"
def notify():
    server = SMTP(SMTP_SERVER,PORT)
    server.starttls()
    server.login(EMAIL_ID,PASSWORD)
    sub="Price Now"
    body="price of stock of Amazon is "+url
    server.sendmail(EMAIL_ID,EMAIL_ID,body)
    server.quit()

if extract_price() <= 10000:
    notify()







