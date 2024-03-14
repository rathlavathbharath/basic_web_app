from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
conn = sqlite3.connect('user_data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users 
             (id INTEGER PRIMARY KEY AUTOINCREMENT, 
             name TEXT, email TEXT, age INTEGER, dob DATE)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    dob = request.form['dob']

    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)''', (name, email, age, dob))
    conn.commit()
    conn.close()

    return redirect(url_for('retrieve'))

@app.route('/retrieve')
def retrieve():
    conn = sqlite3.connect('user_data.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    data = c.fetchall()
    conn.close()
    return render_template('retrieve.html', data=data, submitted=True)

if __name__ == '__main__':
    app.run(debug=True)
