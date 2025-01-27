from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")

mongo_client = MongoClient(MONGO_URI)
