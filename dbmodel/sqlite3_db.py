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
            cursor.execute("CREATE TABLE collection (name text, num integer, img text)")
        cursor.close()
    
    def select(self):
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM collection")
            return cursor.fetchall()
        except:
            return ""

    def insert(self, name, num, img):
        params = {'name':name, 'num':num, 'img':img}
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute("insert into collection (name, num, img) VALUES (:name, :num, :img)", params)
            connection.commit()
            cursor.close()
        except:
            return False
        return True