
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify
from werkzeug.security import generate_password_hash,check_password_hash




app = Flask(__name__)
app.secret_key = 'secretkey'
app.config()
@app.route('/')
def hello():
    return('hello rajendra')

if __name__ == '__main__':
    app.run(debug= True)