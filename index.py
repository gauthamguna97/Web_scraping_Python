import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/trending/"
r1 = requests.get(url)

class News:
  def __init__(self, link, img, title, desc):
    self.link = link
    self.img = img
    self.title = title
    self.desc = desc

coverpage = r1.content
soup1 = BeautifulSoup(coverpage, 'html5lib')
coverpage_news = soup1.find_all('article')
headline = coverpage_news.pop(0)

link = headline.find('a')['href']
img = headline.find('img')['src']
title = headline.find('h2')
desc = headline.find('span', class_="css-351fmf")
inlist = News(link, img, title, desc)

print(link, img, title, desc)
