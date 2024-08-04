from flask_restful import Resource
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from flask import request
from api.constants import JOURNAL_LIST
import time

from db.supabaseHandler import *

class HotNews(Resource):
    def get(self):
        data = getHeadlines(1)
        return data.data

class DetailJournal(Resource):
    def get(self):
        link_param = request.args.get('link')
        journal_id = request.args.get('journal_id')
        try:
            return JOURNAL_LIST[journal_id].getDetail(link_param)
        except: 
            return {}


class InternationalNews(Resource):
    def get(self):
        data = getHeadlines(2)
        return data.data
    # def _shuffle(self, *args):
    #     new_list = []
    #     for i in range(len(args)):
    #         new_list.append(args[i])