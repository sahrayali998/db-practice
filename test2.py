import sqlite3

cnt = sqlite3.connect('db-virgool')

c = cnt.cursor()
c.execute("""
    INSERT INTO user (username, password) VALUES ('ali','sahdas')
""")

cnt.commit()