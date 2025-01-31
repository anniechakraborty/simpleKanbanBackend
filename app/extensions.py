from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt

import os
mongo = PyMongo()
bcrypt = Bcrypt()

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI', '')
mongo = MongoClient(MONGO_URI)
db = mongo['simpleKanban']

jwt_secret_key = os.getenv('JWT_SECRET_KEY ', '')