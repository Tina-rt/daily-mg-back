from flask_restful import Resource
import scraper.olympicscraper as olympicscraper

class Olympics(Resource):
    def get(self):
        return olympicscraper.getTable()