class GoodStock :
    def __init__(self, code, num):
        #상품수량
        self.goodsCode = code
        #재고수량
        self.stockNum = num
    def addStock(self, amount):
        self.stockNum += amount

code = input("상품 코드를 입력하세요 : ")
num = int(input("재고 수량을 입력하세요 : "))

goods1 = GoodStock(code, num)
goods2 = GoodStock(code, num)

print(goods1)

amount = int(input("추가수량 입력 : "))

goods1.addStock(amount)

print(goods1)
print("재고수량 :",goods1.stockNum)