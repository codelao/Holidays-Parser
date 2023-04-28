import requests
import datetime
import sys
import colorama
from db import Database
from bs4 import BeautifulSoup
from urllib.request import urlopen
from termcolor import colored


db = Database('holidays.db')


class App:
    def __init__(self):
        self.check_internet_connection()
        self.parser()

    def check_internet_connection(self):
        try:
            urlopen('https://google.com')
            return True
        except:
            return False

    def parser(self):
        if not self.check_internet_connection() == False:
            colorama.init()
            self.today = datetime.datetime.today()
            self.date = self.today.strftime("%m/%d/%Y")
            self.site_link = 'https://www.checkiday.com/'
            self.get_site = requests.get(self.site_link).text
            self.soup = BeautifulSoup(self.get_site, 'lxml')
            self.holiday = self.soup.find_all('h2')[0].get_text(strip=True)
            db.holiday_add(date=self.date, holiday=self.holiday)
            self.holidays_parsed = db.parsed_holidays()
            print('Today is ' + colored(self.holiday, 'green') + '\nHolidays parsed: ' + colored(self.holidays_parsed, 'blue'))
            sys.exit()
        else:
            print(colored('Check your internet connection', 'red'))
            sys.exit()


if __name__ == '__main__':
    App()