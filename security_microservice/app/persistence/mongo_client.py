import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


uri_connection: str = os.getenv("MONGO_URI", 'localhost:27017')
database_name: str = os.getenv("MONGO_DB", 'security')

mongo_client: MongoClient = MongoClient(f"mongodb://{uri_connection}")

db = mongo_client[database_name]


def get_collection(name: str):
    return db[name]
