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
            cursor.execute("CREATE TABLE collection (email text, name text, num integer, img text, wishlist int)")
        cursor.close()
    
    def select(self, email, wishlist):
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            if wishlist == 'FALSE':
                cursor.execute(f"SELECT * FROM collection WHERE email='{email}' AND wishlist='FALSE'")
            else:
                cursor.execute(f"SELECT * FROM collection WHERE email='{email}' AND wishlist='TRUE'")

            return cursor.fetchall()
        except:
            return ""

    def insert(self, email, name, num, img, wishlist):
        params = {'email':email, 'name':name, 'num':num, 'img':img, 'wishlist':wishlist}
        if name is None or num is None or img is None:
            return False
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute("insert into collection (email, name, num, img, wishlist) VALUES (:email, :name, :num, :img, :wishlist)", params)
            connection.commit()
            cursor.close()
        except:
            return False
        return True
    
    def remove(self, email, name, num, img):
        try:
            connection = sqlite3.connect(DATABASE)
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM collection WHERE email='{email}' AND name='{name}' AND num={num} AND img='{img}'")
            connection.commit()
            cursor.close()
        except:
            return False
        return True