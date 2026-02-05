from flask_restful import Resource
from threading import Thread
import traceback

from scraper import midimdgscraper, expressmadascraper, lemondescraper
from utils.journal_crud import *
from utils.aiSorting import sortNews

def launch():
    try:
        print("Launching scraping")
        all_journal = midimdgscraper.getHotNews() + expressmadascraper.getHotNews() + lemondescraper.getHotNews()
        print(f"Scraped {len(all_journal)} articles total")
        
        journals = sortNews(all_journal)
        print("Sorted journal", journals)
        
        print("Inserting data", len(journals))
        add_journals(journals)
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