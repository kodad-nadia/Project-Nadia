import firebase_admin
import pyrebase
from firebase_admin import credentials
from dotenv import dotenv_values
import json
from configs.firebase_config import firebaseConfig

config = dotenv_values(".env")

if not firebase_admin._apps:
  cred = credentials.Certificate(json.loads(config['FIREBASE_SERVICE_ACCOUNT_KEY']))
  firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
db = firebase.database()
authUser = firebase.auth()

firebase = pyrebase.initialize_app(json.loads(config['FIREBASE_CONFIG']))
db = firebase.database()
authSession = firebase.auth()