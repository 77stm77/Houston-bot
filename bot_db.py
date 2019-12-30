import sqlite3
import json
import datetime

bots_db = "bots_db"
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(bots_db))
c = connection.cursor()
