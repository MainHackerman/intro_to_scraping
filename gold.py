import requests
import bs4

page = requests.get('https://www.bloomberg.com/quote/GC1:COM')

page_soup = bs4.BeautifulSoup(page.text, 'html.parser')
#page_soup.
span = page_soup.find_all('span')
