class Account() :
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = int(balance)
    def deposit(self,amount):
        self.balance += int(amount)
    def withdraw(self,amount):
        if int(self.balance) < int(amount) :
            print("잔액이 부족합니다")
        else :
            self.balance -= int(amount)
    def printAccount(self):
        print("계좌번호 :",self.accountNo)
        print("예금주 이름 :",self.ownerName)
        print("잔액 :",self.balance)

obj1 = Account("111-222-33333333","정수아","50000")
obj2 = Account("555-666-77777777","손이얀","100000")

obj1.deposit(100000)
obj2.withdraw(30000)
obj1.printAccount()
obj2.printAccount()
