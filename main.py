class StockManger:
    
    def __init__(self):
        self.itemList = []
    
    def search(self, search_term):
        low = 0
        high = len(self.itemList) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = self.itemList[mid]
            if search_term in guess.name:
                return self.itemList[mid]
            if guess.name > search_term:
                high = mid - 1
            else:
                low = mid + 1
        return None
    
    def timeLeft(self):
        return 
    
    

class Item():
    def __init__(self, n, s):
        self.name = n
        self.stock = s
        self.age = 0
        self.history = [self.stock]
    def time(self):
        age+=1
        self.history.append(self.stock)

s = StockManger()
s.itemList.append(Item("Chad Juice", 1))
s.itemList.append(Item("Chud Juice", 2))
s.itemList.append(Item("Sigma Juice", 3))
print(s.search("Cha").name)
