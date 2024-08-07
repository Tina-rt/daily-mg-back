import os, sys, json
sys.path.append('../')
import google.generativeai as genai

from db.supabaseHandler import getOnlyTitleId

headlines = getOnlyTitleId()
# print(str(headlines))
# genai.configure(api_key=os.environ['GEMINI_KEY'])

model = genai.GenerativeModel("gemini-1.5-flash")

def predict_top_news(headlines):
    response = model.generate_content("Choose 3 top headlines from these headlines (Just return the results without any other text, just return a list of the index in a array format)" + str(headlines))
    return json.loads(response.text)
