from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise Exception("MONGO_URL is not set in the .env file")

client = MongoClient(MONGO_URL)
db = client["ai_crm"]

persona_collection = db["personas"]
profile_collection = db["profiles"]
match_collection = db["matches"]
