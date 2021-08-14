import sqlite3     

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY, title, link)")
        self.conn.commit()
    
    def fetch(self):
        self.curr.execute("SELECT * FROM links")
        row = self.curr.fetchall()
        return row

    def insert(self, title, link):
        self.curr.execute("INSERT INTO links VALUES (NULL, ?, ?)",(title, link))
        self.conn.commit()
    
    def remove(self, id):
        self.curr.execute("DELETE FROM links WHERE id = ?",(id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('bookmarks.db')
