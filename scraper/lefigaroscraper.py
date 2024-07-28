from bs4 import BeautifulSoup
import requests

JOURNAL_URL = 'https://www.lefigaro.fr/international'

def getHotNews():
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select('.fig-ranking-profile-container')
    result = []
    for article in articles:
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.find('h2').text
        link = article_soup.find('a').attrs['href']
        img_soup = article_soup.find('img')
        
        if img_soup and 'srcset' in img_soup.attrs:
            img = img_soup.attrs['srcset']
        else:
            img = 'no_image'
        data = {
            'journal_id': 2,
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
