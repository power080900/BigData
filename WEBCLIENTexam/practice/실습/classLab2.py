class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    def getBookInfo(self):
        print("책이름 :",str(self.title))
        print("저자 :",str(self.author))
        print("가격 : %s" % format(self.price,","))
    def __str__(self):
        return str("Book 클래스로 생성된 객체")

book1 = Book("파이썬 정복","김상형","22000")
book2 = Book("맛있는 MongoDB","정승호","28000")
book3 = Book("점프 투 장고","박응용","19800")
book4 = Book("생활코딩 HTML+CSS+자바스크립트","이고잉","27000")
book5 = Book("이것이 MariaDB다","우재남","30000")

print("[객체1 :", str(book1) ,"]")
book1.getBookInfo()
print("-"*50)
print("[객체 2 :", str(book2) ,"]")
book2.getBookInfo()
print("-"*50)
print("[객체 3 :", str(book3) ,"]")
book3.getBookInfo()
print("-"*50)
print("[객체 4 :", str(book4) ,"]")
book4.getBookInfo()
print("-"*50)
print("[객체 5 :", str(book5) ,"]")
book5.getBookInfo()