from bs4 import BeautifulSoup
import requests
from utils.journal_crud import article_exists
from utils.image_scraper import get_image as get_image_from_bing

JOURNAL_URL = 'https://www.lemonde.fr/international'

def getHotNews():
    print("Scraping Le Monde")
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select('.teaser__link')
    print("Le Monde: article found", len(articles))
    result = []
    i = 0
    for article in articles:
        i+=1
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.find('h3').text
        link = article.attrs['href']
        img_soup = article_soup.find('img')
        
        if img_soup and 'data-src' in img_soup.attrs:
            img = img_soup.attrs['data-src']
        else:
            img = get_image_from_bing(title) or 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6ik7EhONE0Y90usBK-uXWrq4Q6xcM3dh9Xw&s'
        data = {
            'id': 'lemonde' + str(i),
            'journalId': 3,
            'journal': 'Le Monde',
            'category': 'international',
            'title': title,
            'link': link,
            'img': img,
        }
        # print(data)
        if article_exists(link): 
            print("Article already exists", link)
            continue
        result.append(data)

    # other_articls_soup = soup.select('.teaser--normal')
    return result


def getDetail(link):
    r = requests.get(link)
    soupDetail = BeautifulSoup(r.text, 'html.parser')
    article_content = soupDetail.select_one('div[class="item-post-inner flex-col"]')
    if article_content == None:
        return None
    article_paragraph_list = article_content.find_all('p')



if __name__ == '__main__':
    print(getHotNews())