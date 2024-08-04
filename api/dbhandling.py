from flask_restful import Resource
from db.scraperService import insertScraperData, insertLocalHeadlines, insertInternationalHeadlines

class DbHandler(Resource):
    def get(self):
        insertScraperData()
        return {'msg': 'Data inserted'}


class InsertDb(Resource):
    def get(self, category):
        if category == 1:
            insertLocalHeadlines()
            return {'msg': 'Local Headlines inserted'}
        elif category == 2:
            insertInternationalHeadlines()
            return {'msg': 'International Headlines inserted'}
        else:
            return {'msg': 'Invalid category'}
            
    
    
