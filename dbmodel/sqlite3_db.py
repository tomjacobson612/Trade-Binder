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
            cursor.execute("CREATE TABLE collection (name text, num integer)")
        cursor.close()
    
    def select(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM collection")
        return cursor.fetchall()

    def insert(self, name, num):
        params = {'name':name, 'num':num}
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        cursor.execute("insert into collection (name, num) VALUES (:name, :num)", params)
        connection.commit()
        cursor.close()
        return True