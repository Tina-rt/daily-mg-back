from flask import Flask
from flask_restful import Resource, Api
from scraper import expressmadascraper
from api.journal import *


app = Flask(__name__)
api = Api(app)


api.add_resource(HotNews, '/')
api.add_resource(DetailJournal, '/detail')

if __name__ == '__main__':
    app.run()
