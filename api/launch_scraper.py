from flask_restful import Resource
from threading import Thread

from scraper import midimdgscraper, expressmadascraper
from utils.journal_crud import *


def launch():
    print("Launching scraping")
    all_journal = midimdgscraper.getHotNews()+ expressmadascraper.getHotNews()
    print("Inserting data", len(all_journal))
    add_journals(all_journal)
    print("Launching scraped finished")


class LaunchScraper(Resource):
    def get(self):
        th = Thread(target=launch)
        th.start()
        return {"info": "Scraping launched"}