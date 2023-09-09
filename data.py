from datetime import datetime
import os
class FileStorage:
    def __init__(self, path):
        self.path = path
        if not os.path.isfile(path):
            open(path, 'w').close()
    
    def read(self):
        return open(self.path, 'r').read()
    
    def write(self, content):
        return open(self.path, 'w').write(content)

class Item:
    def __init__(self, name, category, date, cost):
        self.name = name
        self.category = category
        self.date = date
        self.cost = cost

    def to_save_str(self):
        return f"{self.name}\t{self.category}\t{self.date}\t{self.cost}"
    
    @staticmethod
    def from_save_str(save_str):
        name, category, date, cost = save_str.split('\t')
        return Item(name, category, datetime.fromisoformat(date), int(cost))

class ItemList:
    def __init__(self, items, storage):
        self.items = items
        self.storage = storage
    
    def to_save_str(self):
        return '\n'.join(item.to_save_str() for item in self.items)
    
    @staticmethod
    def from_save_str(content):
        if content == '':
            return []
        return [Item.from_save_str(line) for line in content.split('\n')]
    
    @staticmethod
    def load(storage):
        return ItemList(ItemList.from_save_str(storage.read()), storage)
    
    def save(self):
        self.storage.write(self.to_save_str())
    
    def add(self, new_item):
        self.items.append(new_item)
        self.save()