from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

accounts = {}

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance
    
@app.route('/home')
def index():
    return 'Welcome to the Banking System!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in accounts and accounts[username].password == password:
            return redirect(url_for('account', username=username))
        return 'Invalid credentials'
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in accounts:
            accounts[username] = Account(username, password)
            return redirect(url_for('login'))
        return 'Account already exists'
    return render_template('register.html')

@app.route('/account/<username>')
def account(username):
    if username in accounts:
        account = accounts[username]
        return f'Welcome {account.username}! Balance: ${account.check_balance()}'
    return 'Account not found'

@app.route('/deposit/<username>', methods=['GET', 'POST'])
def deposit(username):
    if username in accounts:
        if request.method == 'POST':
            amount = float(request.form['amount'])
            accounts[username].deposit(amount)
            return f'Success! Deposited ${amount}. Your new balance is ${accounts[username].check_balance()}.'
        return render_template('deposit.html')
    return 'Account not found'

@app.route('/withdraw/<username>', methods=['GET', 'POST'])
def withdraw(username):
    if username in accounts:
        if request.method == 'POST':
            amount = float(request.form['amount']) 
            if accounts[username].withdraw(amount):
                return f'Success! Withdrew ${amount}. Your new balance is ${accounts[username].check_balance()}.'
            return 'Insufficient Funds.'
        return render_template('withdraw.html')
    return 'Account not found'

if __name__ == '__main__':
    app.run(debug=True)
