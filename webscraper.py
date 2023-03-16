#following guide: https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
URL = "https://www.geeksforgeeks.org/data-structures/"

r = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())

