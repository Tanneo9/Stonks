import statistics
from typing import List, Optional
import json

class Item:

    # creates item object with name, stock, age, and history of stock levels
    def __init__(self, n: str, s: float, a: int = 0, h: Optional[List[float]] = None) -> None:
        self.name: str = n
        self.stock: float = s
        self.age: int = a
        self.history: List[float] = [self.stock]

    # adds the stock to a history list which tracks the stock levels over time, and increases the age of the item by 1
    def update(self, stock: Optional[float] = None) -> None:
        self.age+=1
        if stock == None:
            self.history.append(self.stock)
        else:
            self.history.append(stock)

class StockManger:
    
    def __init__(self) -> None:
        self._item_list: List[Item] = []

    # returns a sorted list of items by name
    @property
    def item_list(self) -> List[Item]:
        return self._sort_items(self._item_list)
    
    # Uses a binary search to find the item with the name that contains the search term, and returns the item if found, otherwise returns None
    def search(self, search_term: str) -> Optional[Item]:
        low = 0
        high = len(self._item_list) - 1
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
    
    # Uses a merge sort to sort the items by name, and returns the sorted list
    def _sort_items(self, list: Optional[List[Item]] = None) -> List[Item]:
        if list is None:
            list = self._item_list

        half1 = list[:int(len(list)/2):]
        half2 = list[int(len(list)/2)::]

        if not half1:
            return half2     
        return self._merge(self._sort_items(half1), self._sort_items(half2))
    
    # Merges two lists of items from smallest to largest in terms of unicode
    def _merge(self, list1: List[Item], list2: List[Item]) -> List[Item]:
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
    
    # Adds an item to the stock manager, and raises a ValueError if the stock is negative
    def add(self, item: Item) -> None:
        if item.stock < 0:
            raise ValueError("Stock cannot be negative.")
        self._item_list.append(item)
    
    # Calculates the burn rate using the stored item history to get an average slope, and then uses the current stock and the burn rate to calculate the time left until the stock runs out, and returns a string with the result
    def timeLeft(self, iName: str) -> str:
        try:
            item = self.search(iName)
            if item:
                slope = statistics.mean([item.history[time] - item.history[time - 1] for time in range(1, len(item.history))])
                return item.name + ": " + (str(abs(1.0 * item.stock / slope)) if slope < 0 else "Infinite") + " time left"
            else:
                return "Item not found."
        except Exception as e:
            return "Error. Has the item stock changed yet?"
    
    # saves all items in the stock manager to a json file, and raises an exception if there is an error saving the data
    def save(self) -> None:
        try:
            with open("stock_data.json", "w") as f:
                items = [item.__dict__ for item in self.item_list]
                json.dump(items, f, indent=4)
        except Exception as e:
            print(f"Error saving data: {e}")

    # loads all items from a json file, and raises an exception if there is an error loading the data
    def load(self) -> None:
        try:
            with open("stock_data.json", "r") as f:
                items = json.load(f)
                self._item_list = [Item(item["name"], item["stock"], item["age"], item["history"]) for item in items]
        except Exception as e:
            print(f"Error loading data: {e}")

# creating stockmanager and adding data
s = StockManger()
# s.add(Item("Chud Juice", 1))
# s.add(Item("Chad Juice", 2))
# s.add(Item("Sigma Juice", 3))
# s.add(Item("Alpha juice", 4))
s.load()
for item in s.item_list:
    print(item.name)

# printing out a search result
print()
print(f"Seach term: \"s\"\nResult: {s.search("s").name}")
print()

# testing burn rate calculation
s.item_list[0].stock-=2
s.item_list[0].update()
for i in s.item_list:
    print(i.name + " " + str(i.history))
print(s.timeLeft("Alph"))

# s.save()



# Do we use this, if not delete data.txt thats just a asset for testing

# allManagers = []
# try: #loads data.txt and stops if it finds an error
#     with open('data.txt', 'r') as sixseven:
#         content = sixseven.read().strip()
#         for block in re.split(r'\n{2,}', content):
#             pot = StockManger()
#             items = [re.split(r'\n', block)[i*3:i*3+3] for i in range(int(len(re.split(r'\n', block))/3))]
#             for item in items:
#                 pot.add(Item(item[0][:item[0].index(":")], int(item[1][item[1].index(": ")+2:]), [int(i) for i in re.split(r", ",item[2][item[2].index(": ")+3:-1])]))
#             allManagers.append(pot)
# except Exception as e:
#     allManagers = []
#     print("Invalid or no data.txt found (LOADING CANCELED).")

# # add and change managers here and make sure to add all managers to allManagers
# for m in allManagers: 
#     for i in m.item_list:
#         print("Item: " + i.name + " Stock: " + str(i.stock) + " History: " + str(i.history))
#     print("")

# with open('data.txt', 'w') as skibidi: # Saves all managers into data.txt
#     save = ""
#     for m in allManagers:
#         for i in m.item_list:
#             save+=i.name + ":\n\tStock: " + str(i.stock) + "\n\tHistory: " + str(i.history) + "\n"
#         save+=("\n")
#     skibidi.write(save)