#!/usr/bin/env python3

import os, sys, time, datetime, requests, colorama, urllib.request
from bs4 import BeautifulSoup
from db import Database


__path__ = os.path.dirname(__file__)
db = Database(__path__ + '/holidays.db')

class App:
    def __init__(self, mode):
        self.mode = mode
        self.parser()

    def check_internet_connection(self):
        try:
            urllib.request.urlopen('https://google.com', timeout=1)
            return True
        except:
            return False

    def parser(self):
        if self.mode == 1:
            if not self.check_internet_connection() == False:
                try:
                    colorama.init()
                    self.today = datetime.datetime.today()
                    self.date = self.today.strftime("%m/%d/%Y")
                    self.site_link = 'https://www.checkiday.com/'
                    self.get_site = requests.get(self.site_link).text
                    self.soup = BeautifulSoup(self.get_site, 'lxml')
                    self.holiday = self.soup.find_all('h2')[0].get_text(strip=True)
                    db.holiday_add(date=self.date, holiday=self.holiday)
                    self.holidays_parsed = db.parsed_holidays()
                    print('Today is \033[32m' + self.holiday + '\033[0m.' +
                        '\nHolidays parsed: \033[32m' + str(self.holidays_parsed) + '\033[0m')
                    time.sleep(1)
                    sys.exit(0)
                except Exception as e:
                    print(f"\033[31mUnexpected error occured. Printing out the details:\033[0m\n{e}")
                    sys.exit(1)
            else:
                print('\033[31mCheck your internet connection or try again.\033[0m')
                sys.exit(1)


if __name__ == '__main__':
    App(1)
