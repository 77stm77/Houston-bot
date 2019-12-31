import sqlite3

bots_db = "bots_db"
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(bots_db))
c = connection.cursor()


def create_table():
    c.execute("")
