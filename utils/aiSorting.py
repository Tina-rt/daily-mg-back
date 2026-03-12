from enum import Enum
from google import genai
import dotenv, os, sys, time
from pydantic import BaseModel

class TopicEnum(Enum):
    POLITICS = "politics"
    SPORT = "sport"
    ECONOMY = "economy"
    INTERNATIONAL = "international"
    CULTURE = "culture"
    TECHNOLOGY = "technology"
    HEALTH = "health"
    EDUCATION = "education"
    ENTERTAINMENT = "entertainment"
    OTHER = "other"

class News(BaseModel):
    id: str
    title: str
    topic: TopicEnum
    pertinence: int

dotenv.load_dotenv()

client = genai.Client()

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

def sortNews(news: list):
    print("sorting news using gemini ...")
    news_for_ai = [{'id': n['id'], 'title': n['title']} for n in news]
    contents = f'''
    Sort these news by less important news to the most important (Give pertinence score from 1 to 10) and give each news a topic.
    Analyze the title and do not repeat similar news. If you find similar news, remove the less important one.
    {news_for_ai}
'''
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=contents, config={
            "response_mime_type": "application/json",
            "response_schema": list[News]
        }
    )
    print(response.text)
    sorted_news:list[News] = response.parsed
    rslt = []
    for sorted_journal in sorted_news:
        for full_new in news:
            if full_new['id'] == sorted_journal.id:
                full_new['created_at_tm'] = time.time()
                full_new['topic'] = sorted_journal.topic.value
                rslt.append(full_new)
    print("Finish sorting news. Total: ", len(rslt))
    return rslt
