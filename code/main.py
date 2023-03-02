import requests
import datetime
from db import Database
from bs4 import BeautifulSoup


db = Database('holidays.db')

today = datetime.datetime.today()
date = today.strftime("%m/%d/%Y") #today's date


site_link = 'https://www.checkiday.com/'
get_site = requests.get(site_link).text
parse = BeautifulSoup(get_site, 'lxml')

block = parse.find('section', id='magicGrid')
holiday = block.find('h2').get_text(strip=True)

db.holiday_add(date=date, holiday=holiday) #add holiday with it's date to the database
