from bs4 import BeautifulSoup
import requests

JOURNAL_URL = 'https://www.lexpress.mg/'
def getHotNews() -> list:
    r = requests.get(JOURNAL_URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    articles = soup.find_all('article')
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
            result.append({
                'publisher_id': 1,
                'title': title,
                'link': link,
                'img': img,
                'detail': detail,
                'published_at': date,
                'category': 1
                
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
   
    try:article_img = article_content.find('img').attrs['src']
    except: article_img = 'no_image'

    date_ = article_content.find('time').attrs['datetime']
    content = [p.text for p in article_paragraph_list]
    return {
        'content': content,
        'img': article_img,
        'date': date_
    }
