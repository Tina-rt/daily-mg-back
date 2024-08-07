from bs4 import BeautifulSoup
import requests

JOURNAL_URL = 'https://www.lemonde.fr/international'

def getHotNews():
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.select('.teaser__link')
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
            img = 'data:image/jpeg;base64,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'
        data = {
            'publisher': 4,
            'title': title,
            'link': link,
            'img': img,
            'category': 2,
            'isTop': False
        }
        if data['link'] in map(lambda x: x['link'], result):
            continue
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