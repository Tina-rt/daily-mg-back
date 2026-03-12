from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from scraper import expressmadascraper
from api.journal import *
from api.olympics import *
from api.launch_scraper import LaunchScraper

app = Flask(__name__)
api = Api(app)
CORS(app, resources={r"/*": {"origins": "*"}})

api.add_resource(HotNews, '/')
api.add_resource(DetailJournal, '/detail')
api.add_resource(InternationalNews, '/international')
api.add_resource(Olympics, '/olympics')
api.add_resource(LaunchScraper, '/launch')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
