from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnld=109"

result = req.urlopen(url)

soup = BeautifulSoup(result, "html.parser")

title = soup.find("title").string

print(title)