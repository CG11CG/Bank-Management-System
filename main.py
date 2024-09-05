from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

accounts = {}

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def check_balance(self):
        return self.balance
    
    @app.route('/home')
    def index():
        return 'Welcome to the Banking System!'

