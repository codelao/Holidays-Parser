import requests
import datetime
from db import Database
from bs4 import BeautifulSoup


db = Database('holidays.db')

today = datetime.datetime.today()
date = today.strftime("%m/%d/%Y") #today's date

site_link = 'https://www.checkiday.com/'
get_site = requests.get(site_link).text
parser = BeautifulSoup(get_site, 'lxml')
holiday = parser.find_all('h2')[0].get_text(strip=True)

db.holiday_add(date=date, holiday=holiday)