from flask_restful import Resource
from threading import Thread

from scraper import midimdgscraper, expressmadascraper
from utils.journal_crud import *
from utils.aiSorting import sortNews


def launch():
    print("Launching scraping")
    all_journal = midimdgscraper.getHotNews()+ expressmadascraper.getHotNews()
    print(all_journal)
    journals = sortNews(all_journal)
    print("Sorted journal",journals)
    print("Inserting data", len(journals))
    add_journals(journals)
    print("Launching scraped finished")


class LaunchScraper(Resource):
    def get(self):
        th = Thread(target=launch)
        th.start()
        return {"info": "Scraping launched"}