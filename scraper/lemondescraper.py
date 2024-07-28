from bs4 import BeautifulSoup
import requests

JOURNAL_URL = 'https://www.lemonde.fr/international'

def getHotNews():
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select('.teaser__link')
    result = []
    for article in articles:
        article_soup = BeautifulSoup(str(article), 'html.parser')
        title = article_soup.find('h3').text
        link = article.attrs['href']
        img_soup = article_soup.find('img')
        
        if img_soup and 'data-src' in img_soup.attrs:
            img = img_soup.attrs['data-src']
        else:
            img = 'no_image'
        data = {
            'title': title,
            'link': link,
            'img': img,
        }
        # print(data)
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