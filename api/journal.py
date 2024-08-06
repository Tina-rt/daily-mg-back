from flask_restful import Resource
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from db.supabaseHandler import getDetails
from flask import request
from api.constants import JOURNAL_LIST, CAN_FETCH_DETAILS
import time

from db.supabaseHandler import *

class AllNews(Resource):
    def get(self):
        data = getHeadlines()
        return data.data

class LocalNews(Resource):
    def get(self):
        data = getHeadlines(1)
        return data.data

class DetailJournal(Resource):
    def get(self, id):
       
        data = getDetails(id)
        print(data)
        if len(data) > 0:
            current_headlines = data[0]
            result = {}
            if current_headlines['publisher']['id'] == 2:
                result = midimdgscraper.getDetail(current_headlines['link'])
            elif current_headlines['publisher']['id'] == 1:
                result = expressmadascraper.getDetail(current_headlines['link'])
            else:
                return {}
            result['title'] = current_headlines['title']
            return result
        return {}    


class InternationalNews(Resource):
    def get(self):
        data = getHeadlines(2)
        return data.data
    # def _shuffle(self, *args):
    #     new_list = []
    #     for i in range(len(args)):
    #         new_list.append(args[i])