from bs4 import BeautifulSoup
import requests, json

BASEURL = 'https://olympics.com/en/paris-2024/medals'

def getTable():
    r = requests.get(BASEURL, headers={
        "User-agent": "PostmanRuntime/7.40.0"
    })
    soup = BeautifulSoup(r.text, 'html.parser')
    
    script_soup = soup.find('script', {'id': '__NEXT_DATA__'})
    parsed_data = json.loads(script_soup.text)
    medal_standing = parsed_data['props']['pageProps']['initialMedals']['medalStandings']['medalsTable']
    return medal_standing
    
