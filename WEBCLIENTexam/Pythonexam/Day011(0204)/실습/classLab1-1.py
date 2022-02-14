class Member:
    def __init__(self, name, account, passwd, birthyear):
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear

members = [
    Member("홍길동", "hong","a1234","1988.8.8"),
    Member("이순신", "lee","b5678","1999.9.9"),
    Member("유관순", "you","c9012","1977.7.7")
]

for i, people in enumerate(members,1):
    print(f"회원{i}: {people.name}({people.account},{people.passwd}.{people.birthyear})")