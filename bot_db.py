import sqlite3
import json
import datetime

timeframe = 'bot_db'
sql_transaction = []

connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()
