class Book:
    def __init__(self, title, author, price):
        self.title = str(title)
        self.author = str(author)
        self.price = int(price)
    def getBookInfo(self)->str:
        return self.title+','+self.author+','+str(self.price)
    def __str__(self):
        return str("Book 클래스로 생성된 객체")

book1 = Book("파이썬 정복","김상형","22000")
book2 = Book("맛있는 MongoDB","정승호","28000")
book3 = Book("점프 투 장고","박응용","19800")
book4 = Book("생활코딩 HTML+CSS+자바스크립트","이고잉","27000")
book5 = Book("이것이 MariaDB다","우재남","30000")

print("[객체1 :", str(book1) ,"]")
a,b,c= book1.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*50)
print("[객체2 :", str(book2) ,"]")
a,b,c= book2.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*50)
print("[객체3 :", str(book3) ,"]")
a,b,c= book3.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*50)
print("[객체4 :", str(book4) ,"]")
a,b,c= book4.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*50)
print("[객체5 :", str(book5) ,"]")
a,b,c= book5.getBookInfo().split(",")
print(a,b,c,sep="\n")
print("-"*50)
