from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <ul>
            <li><a href="http://www.naver.com">네이버</a></li>
            <li><a href="http://www.google.com">구글</a></li>
            <li><a href="http://www.daum.net">다음</a></li>
        </ul>
        <h1 id = "title1" class="hello">안녕하세요1</h1>
        <h1 id = "title2" class="hello">안녕하세요2</h1>
        <h1 id = "title3" class="hello">안녕하세요3</h1>
        <p id = "name">이경재입니다</p>
    </body>
    </html>    
"""

# html 태그분석
soup = BeautifulSoup(html, 'html.parser')
list = soup.find_all("a")

for i in list:
    text = i.string
    print(text)

for i in list:
    href = i.attrs["href"]
    print(href)

for i in list:
    href = i.get("href")
    print(href)

title = soup.select_one("h1.hello")
print("title :",title.string)