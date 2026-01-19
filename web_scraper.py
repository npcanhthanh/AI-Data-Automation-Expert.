import requests
from bs4 import BeautifulSoup

def simple_scraper(url):
    """
    Thu thập tiêu đề bài báo tự động để tạo tập dữ liệu AI.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [t.get_text() for t in soup.find_all('h2')]
    return titles

print("Web Scraper is active. Ready to extract data.")
