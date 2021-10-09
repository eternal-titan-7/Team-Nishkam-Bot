from os import getenv

import firebase_admin
import yaml
from dotenv import load_dotenv
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Client

load_dotenv()

cred = credentials.Certificate(yaml.load(getenv("FirestoreCredentials"), Loader=yaml.Loader))
firebase_admin.initialize_app(cred)
db: Client = firestore.client()
