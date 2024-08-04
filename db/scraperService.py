
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from db.supabaseHandler import insertHeadlines
from utils.heandlinesCleaner import clean

def insertInternationalHeadlines():
    insertHeadlines(clean(lemondescraper.getHotNews() + lefigaroscraper.getHotNews()))

def insertLocalHeadlines():
    insertHeadlines(clean(midimdgscraper.getHotNews() + expressmadascraper.getHotNews()))
    
def insertScraperData():
    insertInternationalHeadlines()
    insertLocalHeadlines()

