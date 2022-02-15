from urllib import request as req
from bs4 import BeautifulSoup

url = "https://news.daum.net/"
result = req.urlopen(url)
soup = BeautifulSoup(result, "html.parser")
news = soup.select("strong.tit_g")
for list in news:
    a = list.select_one("a")
    title = a.string
    print("제목 :",title.strip())
    print("링크 :",a.get('href'))