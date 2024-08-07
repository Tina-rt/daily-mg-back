
from scraper import midimdgscraper, expressmadascraper, lemondescraper, lefigaroscraper
from db.supabaseHandler import insertHeadlines
from utils.heandlinesCleaner import clean
from ai.classifier import predict_top_news

def insertInternationalHeadlines():
    insertHeadlines(clean(lemondescraper.getHotNews() + lefigaroscraper.getHotNews()))

def insertLocalHeadlines():
    cleaned_data = clean(midimdgscraper.getHotNews() + expressmadascraper.getHotNews())
    top_news_ids = predict_top_news(cleaned_data)
    for id_ in top_news_ids:
        cleaned_data[id_]['isTop'] = True
    # print(cleaned_data)
    insertHeadlines(cleaned_data)
    
def insertScraperData():
    insertInternationalHeadlines()
    insertLocalHeadlines()

