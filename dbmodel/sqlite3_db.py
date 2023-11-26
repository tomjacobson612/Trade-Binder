from .Model import Model
import sqlite3
DATABASE = 'collection.db'

class model(Model):
    def __init__(self):
        connection = sqlite3.connect(DATABASE)
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM collection")
        except sqlite3.OperationalError:
            cursor.execute("CREATE TABLE collection (email text, name text, num integer, img text)")
        cursor.close()
    
    def select(self, email):
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM collection WHERE email='{email}'")
            return cursor.fetchall()
        except:
            return ""

    def insert(self, email, name, num, img):
        params = {'email':email, 'name':name, 'num':num, 'img':img}
        if name is None or num is None or img is None:
            return False
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute("insert into collection (email, name, num, img) VALUES (:email, :name, :num, :img)", params)
            connection.commit()
            cursor.close()
        except:
            return False
        return True