from bs4 import BeautifulSoup
import requests
from utils.journal_crud import *
import uuid
import datetime, re, dateparser

JOURNAL_URL = 'https://www.madagascar-tribune.com/'

def getHotNews(): 
    print("Scraping Madagascar tribune")
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article')
    # print("Total articles", articles)
    result = []
    i = 0
    for article in articles:
        i+=1
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.select_one('.titre_sommaire').text
        link = article_soup.select_one('a').attrs['href']
        date = ''
        date_author_soup = article_soup.select_one('div.date_auteur')
        if date_author_soup != None:
            date = re.search(r'^([^|]+)', date_author_soup.text.replace('\n', '').strip()).group(1).strip()
            date = dateparser.parse(date)


        try:

            img_soup = article_soup.select_one('img')
        except:
            pass
        if img_soup == None:
            img = 'no_image'
            continue
        else:
            img = JOURNAL_URL + img_soup.attrs['src']
        journal = {
            'id': 'madagascar-tribune-'+str(uuid.uuid4()),
            'journal': 'Madagascar Tribune',
            'created_at': datetime.datetime.now(tz=datetime.timezone.utc),
            'detail': '',

            'title': title,
            'link': link,
            'img': img,
            'published_at': date,
            'publisher': {
                'id': 1,
                'name': 'Madagascar Tribune'
            },
            'category': 'local'
        }
        if article_exists(link): continue
        result.append(journal)
    print("Total madagascar tribune news", len(result))
    return result

def getDetail(link):
    pass
