from bs4 import BeautifulSoup
import requests

JOURNAL_URL = 'https://www.lexpress.mg/'
r = requests.get(JOURNAL_URL)
soup = BeautifulSoup(r.text, 'html.parser')
def getHotNews() -> list:
    articles = soup.find_all('article')
    result = []
    # print(articles)
    for article in articles:
        article_soup = BeautifulSoup(str(article), 'html.parser')
        try:
            title = article.a.attrs['title']
            link = article.a.attrs['href']
            img = article_soup.find(class_='entry-image').attrs['data-image']
            date_soup = article_soup.find('time')
            date = ''
            if date_soup != None: date = date_soup.attrs['datetime'] 
            detail = article_soup.find('p').text
            result.append({
                'journal': 'L\'Express de Madagascar',
                'journalId': 0,
                'title': title,
                'link': link,
                'img': img,
                'detail': detail,
                'date': date
            })
        except: 
            pass
        # print(article.a)
        # pass
    return result

def getDetail(link):
    r = requests.get(link)
    soupDetail = BeautifulSoup(r.text, 'html.parser')
    article_content = soupDetail.select_one('div[class="item-post-inner flex-col"]')
    if article_content == None:
        return None
    article_paragraph_list = article_content.find_all('p')
    article_paragraph = '\n\n'.join([p.text for p in article_paragraph_list])
    article_img = soupDetail.find('img').attrs['src']

    date_ = soupDetail.find('time').attrs['datetime']
    return {
        'content': article_paragraph,
        'img': article_img,
        'date': date_
    }
