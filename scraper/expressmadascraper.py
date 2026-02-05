from bs4 import BeautifulSoup
import requests, uuid, datetime
from utils.journal_crud import article_exists

JOURNAL_URL = 'https://www.lexpress.mg/'
def getHotNews() -> list:
    print("Scraping express de madagascar", JOURNAL_URL)
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article')
    print("Express: article found", len(articles))
    result = []
    i = 0
    # print(articles)
    for article in articles:
        i+=1
        article_soup = BeautifulSoup(str(article), 'html.parser')
        try:
            title = article.a.attrs['title']
            link = article.a.attrs['href']
            img = article_soup.find(class_='entry-image').attrs['data-image']
            date_soup = article_soup.find('time')
            date = ''
            if date_soup != None: date = date_soup.attrs['datetime'] 
            detail = article_soup.find('p').text
            if article_exists(link): 
                print("Article already exists", link)
                continue
            result.append({
                'id': 'midi-'+str(uuid.uuid4()),
                'publisher': {
                    'id': 2,
                    'name': 'L\'Express de Madagascar'
                },
                'title': title,
                'created_at': datetime.datetime.now(tz=datetime.timezone.utc),
                'link': link,
                'img': getHighResImage(link) or img,
                'detail': detail,
                'published_at': date,
                'category': 'local'
            })
        except Exception as e: 
            print(e)
        # print(article.a)
        # pass
    return result


def getHighResImage(link):
    try:
        detailled_article = getDetail(link)
        return detailled_article['img']
    except:
        return None

def getDetail(link):
    r = requests.get(link)
    soupDetail = BeautifulSoup(r.text, 'html.parser')
    article_content = soupDetail.select_one('div[class="item-post-inner flex-col"]')
    if article_content == None:
        return None
    article_paragraph_list = article_content.find_all('p')
   
    try:article_img = article_content.find('img').attrs['src']
    except: article_img = 'no_image'

    date_ = article_content.find('time').attrs['datetime']
    content = [p.text for p in article_paragraph_list]
    return {
        'content': content,
        'img': article_img,
        'date': date_
    }


if __name__ == '__main__':
    print(getHotNews())