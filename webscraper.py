#following guide: https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
import requests

URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)