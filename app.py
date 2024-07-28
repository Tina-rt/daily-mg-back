from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from scraper import expressmadascraper
from api.journal import *


app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


api.add_resource(HotNews, '/')
api.add_resource(DetailJournal, '/detail')
api.add_resource(InternationalNews, '/international')

if __name__ == '__main__':
    app.run(debug=True)
