import sqlite3


class Database:
    def __init__(self, db_file):
        self.con = sqlite3.connect(db_file, check_same_thread=False)

    def quote_add(self, quote):
        with self.con:
            self.con.cursor().execute("INSERT INTO quotes VALUES (?)", (quote,))