import requests
import datetime
from db import Database
from bs4 import BeautifulSoup


db = Database('quotedb.db')


today = datetime.datetime.today()
date = today.strftime("%m/%d/%Y") #today's date


site_link = 'https://thedailyquotes.com/quote-of-the-day/'
get_site = requests.get(site_link).text
bs = BeautifulSoup(get_site, 'lxml')

block = bs.find('div', id="fl-main-content")

result = block.find('h3').get_text(strip=True)
response = f'{date}: {result}' #today's date: Quote of the day
db.quote_add(response) #add response result to database