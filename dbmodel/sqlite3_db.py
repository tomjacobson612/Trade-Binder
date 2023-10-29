from .Model import Model
import sqlite3
DATABASE = 'collection.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM collection")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE collection (name text)")
        cursor.close()
    
    def select(self):
        pass

    def insert(self):
        pass