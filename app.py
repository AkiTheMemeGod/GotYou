from flask import Flask
import sqlite3 as sq


app = Flask(__name__)
con = sq.connect('database.db')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
