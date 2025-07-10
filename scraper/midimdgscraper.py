from bs4 import BeautifulSoup
import requests
from utils.journal_crud import *
import uuid
from threading import Thread
import datetime

JOURNAL_URL = 'https://midi-madagasikara.mg/'

def getHotNews(): 
    print("Scraping midi madagascar")
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all(class_='td-module-container')
    result = []
    i = 0
    for article in articles:
        i+=1
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.find('h3').text
        link = article_soup.find('a').attrs['href']
        date = ''
        date_soup = article_soup.find('time')
        if date_soup != None:
            date = date_soup.attrs['datetime']
        try:

            img_soup = article_soup.select_one('span[data-type="css_image"]')
        except:
            pass
        if img_soup == None:
            img = 'no_image'
            continue
        else:
            img = img_soup.attrs['data-img-url']
        journal = {
            'id': 'midi-'+str(uuid.uuid4()),
            'journal': 'Midi Madagasikara',
            'created_at': datetime.datetime.now(tz=datetime.timezone.utc),
            'detail': '',

            'title': title,
            'link': link,
            'img': img,
            'published_at': date,
            'publisher': {
                'id': 1,
                'name': 'Midi Madagasikara'
            }
        }
        result.append(journal)
    return result

def getDetail(link):
    r = requests.get(link)
    soupDetail = BeautifulSoup(r.text, 'html.parser')
    date = soupDetail.find(class_='entry-date updated td-module-date').text
    
    article_content = soupDetail.find(class_='td_block_wrap tdb_single_content tdi_68 td-pb-border-top td_block_template_1 td-post-content tagdiv-type')
    all_paragraph = article_content.find_all('p')


    try:img_url = article_content.find('img').attrs['src']
    except: img_url = 'no_image'
    print(all_paragraph)
    
    return {
        'date': date,
        'content': [p.text for p in all_paragraph],
        'img': img_url
    }
