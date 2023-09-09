from data import *
from datetime import datetime

storage = FileStorage('/home/tumbochka/pokupki.txt')
item_list = ItemList.load(storage)
a = Item('apples', 'asdf', datetime.now(), 100)

item_list.add(a)
item_list.add(a)