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
        self.id = None


    def to_save_str(self):
        return f"{self.id}\t{self.name}\t{self.category}\t{self.date}\t{self.cost}"
    

    @staticmethod
    def from_save_str(save_str):
        item_id, name, category, date, cost = save_str.split('\t')
        new_item = Item(name, category, datetime.fromisoformat(date), int(cost))
        new_item.id = int(item_id)
        return new_item

    
    def to_str(self):
        return ' | '.join((
            str(self.id),
            self.name,
            self.category,
            self.date.strftime('%d.%m.%y'),
            str(self.cost)
        ))


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
    

    def get_items(self):
        return self.items


    def add(self, new_item):
        new_item.id = self.get_last_id() + 1
        self.items.append(new_item)
        self.save()
    

    def get_categories(self):
        return set(item.category for item in self.items)
    

    def get_last_id(self):
        return max((item.id for item in self.items), default = 0)
    

    def get_by_id(self, item_id):
        try:
            return next(item for item in self.items if item.id == item_id)
        except StopIteration:
            raise KeyError
    

    def delete(self, item_id):
        len1 = len(self.items)
        self.items = [item for item in self.items if item.id != item_id]
        if len1 == len(self.items): # no item with id item_id
            raise KeyError
        self.save()
