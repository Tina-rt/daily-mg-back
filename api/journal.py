from flask_restful import Resource
from scraper import midimdgscraper, expressmadascraper
from flask import request

class HotNews(Resource):
    def get(self):
        return midimdgscraper.getHotNews()+ expressmadascraper.getHotNews()

class DetailJournal(Resource):
    def get(self):
        link_param = request.args.get('link')
        journal_id = request.args.get('journal_id')
        try:
            if journal_id == '1':
                return midimdgscraper.getDetail(link_param)
            elif journal_id == '0':
                return expressmadascraper.getDetail(link_param)
            else:
                return {}
        except: 
            return {}