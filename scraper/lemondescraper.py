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
        
        if img_soup and 'src' in img_soup.attrs:
            img = img_soup.attrs['src']
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


