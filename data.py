from datetime import datetime
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
