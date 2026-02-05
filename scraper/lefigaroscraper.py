from bs4 import BeautifulSoup
import requests
from utils.journal_crud import article_exists
from utils.image_scraper import get_image as get_image_from_bing

JOURNAL_URL = 'https://www.lefigaro.fr/international'

def getHotNews():
    try:
        r = requests.get(JOURNAL_URL)
    except:
        return []
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select('.fig-ranking-profile-container')
    result = []
    i = 0
    for article in articles:
        i += 1
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.find('h2').text
        link = article_soup.find('a').attrs['href']
        img_soup = article_soup.find('img')
        if article_exists(link): continue
        
        if img_soup and 'srcset' in img_soup.attrs:
            img = img_soup.attrs['srcset']
            img = img.split(',')[0]
            img = img[:len(img)-5]
        else:
            img = get_image_from_bing(title) or 'https://logowik.com/content/uploads/images/lefigaro1727.logowik.com.webp'
        data = {
            'id': 'figaro' + str(i),
            'journalId': 2,
            'journal': 'Le figaro',
            'category': 'international',
            'title': title,
            'link': link,
            'img': img,
        }
        result.append(data)
    return result

def getDetail(link):
    r = requests.get(link)
    soupDetail = BeautifulSoup(r.text, 'html.parser')
    article_content = soupDetail.select_one('article')
    article_paragraph_list = article_content.find_all('p')
    
    article_paragraph_txt = [p.text for p in article_paragraph_list]
    return article_paragraph_txt
