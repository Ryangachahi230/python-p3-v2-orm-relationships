import sqlite3

CONN = sqlite3.connect(':memory:')  # use in-memory DB for testing
CURSOR = CONN.cursor()
