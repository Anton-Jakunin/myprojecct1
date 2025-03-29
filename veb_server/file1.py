import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute("CREATE TABLE user (name text, email text)")
c.execute("INSERT INTO user VALUES ('mike', 'mike@mike.com')")
conn.commit()
conn.close()