import sqlite3
import json
import datetime

bots_db = "bots_db"
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(bots_db))
c = connection.cursor()

def create_table():
    c.execute("")

if __name__ == '__main__':
    create_table()
