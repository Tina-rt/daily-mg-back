from flask_restful import Resource
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from flask import request
from api.constants import JOURNAL_LIST

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
        return lefigaroscraper.getHotNews()