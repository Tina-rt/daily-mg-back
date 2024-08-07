from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from scraper import expressmadascraper
from api.journal import *
from api.olympics import *
from api.dbhandling import *
from db.scraperService import *


app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})


api.add_resource(AllNews, '/')
api.add_resource(LocalNews, '/local')
api.add_resource(DetailJournal, '/detail/<int:id>')
api.add_resource(InternationalNews, '/international')
api.add_resource(Olympics, '/olympics')
api.add_resource(DbHandler, '/updateDb')
api.add_resource(InsertDb, '/updateDb/<int:category>')


if __name__ == '__main__':
    app.run(debug=False)
