from pymongo import MongoClient
from bson.json_util import dumps
import json

client = MongoClient("mongodb://tina:tinatina21@172.245.54.65:27017/?authSource=admin")

db = client['dailymg']
collection = db['journals']

try:
    collection.create_index('link', unique=True)
except Exception as e:
    print("Creating unique index failed", e)

def add_journals(journal_data: list):
    for journal in journal_data:
        if article_exists(journal['link']): return
        try:
            print("Inserting journal", journal)
            collection.insert_one(journal)
            print("Journal insertion done")
        except Exception as e:
            print("Inserting failed", e)


def article_exists(journal_link: str):
    j = collection.find_one({"link": journal_link})
    return j is not None

def get_all_journal():
    all_j = collection.find().sort({'created_at', -1}).limit(20)
    
    return json.loads(dumps(all_j))
