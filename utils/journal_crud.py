from pymongo import MongoClient, DESCENDING
from bson.json_util import dumps
import json
from dotenv import load_dotenv
import os
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client['dailymg']
collection = db['articles']

# Check if index exists before creating
indexes = collection.index_information()
index_exists = any(info['key'] == [('link', 1)] for info in indexes.values())

if not index_exists:
    try:
        collection.create_index('link', unique=True)
    except Exception as e:
        print("Creating unique index failed", e)
else:
    print("Index on 'link' already exists.")

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
    all_j = collection.find().sort('created_at_tm', DESCENDING).limit(20)
    
    return json.loads(dumps(all_j))
