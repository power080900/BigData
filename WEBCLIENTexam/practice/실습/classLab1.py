class Member:
    def __init__(self, name, account, passwd, birthyear):
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear
    # def info(self):
    #     print("회원 :",str(self.name)+"("+str(self.account)+","+str(self.passwd)+","+str(self.birthyear)+")")

member1 = Member("홍길동", "hong","a1234","1988.8.8")
member2 = Member("이순신", "lee","b5678","1999.9.9")
member3 = Member("유관순", "you","c9012","1977.7.7")

print("회원 1 :",member1.name+"("+member1.account+","+member1.passwd+","+member1.birthyear+")")
print("회원 2 :",member2.name+"("+member2.account+","+member2.passwd+","+member2.birthyear+")")
print("회원 3 :",member3.name+"("+member3.account+","+member3.passwd+","+member3.birthyear+")")
# member1.info()
# member2.info()
# member3.info()

