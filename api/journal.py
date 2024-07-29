from flask_restful import Resource
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from flask import request
from api.constants import JOURNAL_LIST
import random

class HotNews(Resource):
    def get(self):
        return midimdgscraper.getHotNews()+ expressmadascraper.getHotNews()

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
        lefigaro_list = lefigaroscraper.getHotNews()
        lemonde_list = lemondescraper.getHotNews()
        shuffled = [*lefigaro_list[2:], *lemonde_list[2:]]
        random.shuffle(shuffled)
        return [lefigaro_list[0], lemonde_list[0], lefigaro_list[1], lemonde_list[1],*shuffled ]
    
    # def _shuffle(self, *args):
    #     new_list = []
    #     for i in range(len(args)):
    #         new_list.append(args[i])