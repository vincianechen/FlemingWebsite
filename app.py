from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

@app.route('/login')
def login():
    return 'login'