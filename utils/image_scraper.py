
import requests
from bs4 import BeautifulSoup
import json
import urllib.parse


def is_valid_image(url: str):
    """
    Verifies if the URL is accessible and returns an image type.
    """
    try:
        # Use HEAD request to save bandwidth
        response = requests.head(url, timeout=5, allow_redirects=True)
        
        # Some servers don't support HEAD or return 405/403, try GET if HEAD fails
        if response.status_code != 200:
            response = requests.get(url, timeout=5, allow_redirects=True, stream=True)
            
        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            return content_type.startswith('image/')
    except Exception:
        pass
    return False

def get_image(keyword: str):
    """
    Fetches the first valid image URL from Bing Search for the given keyword.
    """
    print("[Image Scraper] Scraping image for", keyword)
    # Encode the keyword for the URL
    query = urllib.parse.quote_plus(keyword)
    url = f"https://www.bing.com/images/search?q={query}"
    
    # Headers to mimic a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
            
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('a', class_='iusc')
        
        # Try the first 5 images to find one that is actually accessible
        count = 0
        for a in items:
            if count >= 5: break
            
            m_attr = a.get('m')
            if m_attr:
                try:
                    m_data = json.loads(m_attr)
                    murl = m_data.get('murl')
                    if murl and murl.startswith('http'):
                        # Verify the image is accessible
                        if is_valid_image(murl):
                            print("[Image Scraper] Found image for", keyword, murl)
                            return murl
                        count += 1
                except json.JSONDecodeError:
                    continue
                    
    except Exception as e:
        print(f"Error scraping image for '{keyword}': {e}")
        
    return None

if __name__ == '__main__':
    keyword = 'Madagascar landscape'
    print(f"Searching image for: {keyword}")
    img_url = get_image(keyword)
    print(f"Result: {img_url}")