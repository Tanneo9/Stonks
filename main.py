import statistics

class StockManger:
    
    def __init__(self):
        self.item_list = []
    
    def search(self, search_term):
        low = 0
        high = len(self.item_list) - 1
        while low <= high:
            mid = (low + high) // 2
            guess = self.item_list[mid]
            if search_term.lower() in guess.name.lower():
                return self.item_list[mid]
            if guess.name.lower() > search_term.lower():
                high = mid - 1
            else:
                low = mid + 1
        return None
    
    def _sort_items(self, list=None):
        if list is None:
            list = self.item_list

        half1 = list[:int(len(list)/2):]
        half2 = list[int(len(list)/2)::]

        if not half1:
            return half2     
        return self._merge(self._sort_items(half1), self._sort_items(half2))
    
    def _merge(self, list1, list2):
        temp_list = []
        index1 = 0
        index2 = 0
        while index1 < len(list1) or index2 < len(list2):
            item1 = chr(0x10FFFF) 
            item2 = chr(0x10FFFF)
            
            if list1 is not None and len(list1) > index1:
                item1 = list1[index1].name
            if list2 is not None and len(list2) > index2:
                item2 = list2[index2].name

            if item1 > item2:
                temp_list.append(list2[index2])
                index2 += 1
            elif item1 <= item2:
                temp_list.append(list1[index1])
                index1 += 1
        return temp_list
    
    def updateAll(self):
        for i in s.item_list:
            i.update()
        
    def add(self, item):
        self.item_list.append(item)
        self.item_list = self._sort_items(self.item_list)
    
    def timeLeft(self, item):
        try:
            slope = statistics.mean([item.history[time] - item.history[time - 1] for time in range(1, len(item.history))])
            return (str(abs(1.0 * item.stock / slope)) if slope < 0 else "Infinite") + " time left"
        except Exception as e:
            print(e)
    
class Item:

    def __init__(self, n, s):
        self.name = n
        self.stock = s
        self.age = 0
        self.history = [self.stock]

    def time(self):
        age+=1
        self.history.append(self.stock)

    def update(self, stock = None):
        self.age+=1
        if stock == None:
            self.history.append(self.stock)
        else:
            self.history.append(stock)

s = StockManger()
s.add(Item("Chud Juice", 1))
s.add(Item("Chad Juice", 2))
s.add(Item("Sigma Juice", 3))
s.add(Item("Alpha juice", 0))
for item in s.item_list:
    print(item.name)
print()
print(f"Seach term: \"s\"\nResult: {s.search("s").name}")
for i in s.item_list:
    print(i.name + " " + str(i.history))