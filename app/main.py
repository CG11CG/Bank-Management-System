from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': '2001', 
    'host': 'localhost',  
    'database': 'bank_management'
}

def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/home')
def index():
    return 'Welcome to the Banking System!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
            user = cursor.fetchone()

            if user:
                return redirect(url_for('account', username=username))
            return 'Invalid credentials'
        return 'Database connection error'

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            user = cursor.fetchone()

            if user:
                return 'Account already exists'

            cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, password))
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('login'))
        return 'Database connection error'

    return render_template('register.html')

@app.route('/account/<username>')
def account(username):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            user_id, username, password, created_at = user
            return f'Welcome {username}! Your account was created at {created_at}.'
        return 'Account not found'

    return 'Database connection error'

@app.route('/deposit/<username>', methods=['GET', 'POST'])
def deposit(username):
    if request.method == 'POST':
        amount = float(request.form['amount'])

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            # Update the balance in the database
            cursor.execute('UPDATE users SET balance = balance + %s WHERE username = %s', (amount, username))
            conn.commit()

            cursor.close()
            conn.close()

            return f'Success! Deposited ${amount}.'
        return 'Database connection error'

    return render_template('deposit.html')

@app.route('/withdraw/<username>', methods=['GET', 'POST'])
def withdraw(username):
    if request.method == 'POST':
        amount = float(request.form['amount'])

        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            # Check if the balance is sufficient
            cursor.execute('SELECT balance FROM users WHERE username = %s', (username,))
            balance = cursor.fetchone()

            if balance and balance[0] >= amount:
                # Withdraw amount
                cursor.execute('UPDATE users SET balance = balance - %s WHERE username = %s', (amount, username))
                conn.commit()

                cursor.close()
                conn.close()

                return f'Success! Withdrew ${amount}.'
            elif balance:
                return 'Insufficient Funds.'
            else:
                return 'Account not found.'

        return 'Database connection error'

    return render_template('withdraw.html')

@app.route('/test-db')
def test_db():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        conn.close()
        return render_template('test_db.html', rows=rows)

    return 'Database connection error'

if __name__ == '__main__':
    app.run(debug=True)

