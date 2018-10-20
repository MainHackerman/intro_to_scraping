import requests
import bs4

r = requests.get('https://httpbin.org/')
text = r.text
#print(text)
soup_obj = bs4.BeautifulSoup(text, 'html.parser')
search = soup_obj.find_all('h2')
print(type(search))



