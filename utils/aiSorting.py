from google import genai
import dotenv, os, sys, time
from pydantic import BaseModel

class News(BaseModel):
    id: str
    title: str

dotenv.load_dotenv()

client = genai.Client()

GEMINI_API_KEY = os.environ['GEMINI_API_KEY']

def sortNews(news: list):
    print("sorting news using gemini ...")
    news_for_ai = [{'id': n['id'], 'title': n['title']} for n in news]
    contents = f'''
    Sort these news by pertinence
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
                rslt.append(full_new)
    return rslt
