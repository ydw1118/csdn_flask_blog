# coding:utf8

from flask import Flask
from config import Devconfig

app = Flask(__name__)

# Get the config from object of DevConfig


@app.route('/')
def home():
    return '<h1>HHHHHHH</h1>'


if __name__ == '__main__':
    app.run()