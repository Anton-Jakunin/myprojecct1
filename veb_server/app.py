from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def index():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    a = c.execute("SELECT * FROM user")
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        c.execute(f"INSERT INTO user VALUES ({name}, {email})")
    conn.commit()
    conn.close()
    return render_template('index.html', name = a)