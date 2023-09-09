from data import Item
from datetime import datetime

a = Item('apples', 'asdf', datetime.now(), 100)
a_clone = Item.from_save_str(a.to_save_str())
assert(a.to_save_str() == a_clone.to_save_str())