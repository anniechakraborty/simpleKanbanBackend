from flask_pymongo import PyMongo
from pymongo import MongoClient
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

import os
mongo = PyMongo()
bcrypt = Bcrypt()
jwt = JWTManager()

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI', '')
mongo = MongoClient(MONGO_URI)
db = mongo['simpleKanban']