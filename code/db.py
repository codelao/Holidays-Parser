import sqlite3


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS holidays(date TEXT PRIMARY KEY, holiday TEXT)")

    def holiday_add(self, date, holiday):
        with self.con:
            self.con.cursor().execute("INSERT INTO holidays VALUES (?, ?)", (date, holiday,))
