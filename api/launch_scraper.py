from flask_restful import Resource
from threading import Thread
import traceback
import pprint as pp

from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper, madagascartribune
from utils.journal_crud import *
from utils.aiSorting import sortNews

def launch():
    try:
        print("Launching scraping")
        local_news = (midimdgscraper.getHotNews() + expressmadascraper.getHotNews() + madagascartribune.getHotNews())
        Thread(target=lambda: add_journals(sortNews(local_news)), daemon=True).start()
        
        international_news = (lefigaroscraper.getHotNews() + lemondescraper.getHotNews())
        print(f"Scraped international news: {len(international_news)} articles total")
        Thread(target=lambda: add_journals(sortNews(international_news)), daemon=True).start()
        
        print("Launching scraped finished")
    except Exception as e:
        print(f"Error in scraping thread: {e}")
        traceback.print_exc()


class LaunchScraper(Resource):
    def get(self):
        try:
            th = Thread(target=launch)
            th.daemon = True
            th.start()
            return {"status": "success", "message": "Scraping launched in background"}, 200
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500