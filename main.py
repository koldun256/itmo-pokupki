from data import *
from cli.menu import start
from datetime import datetime

storage = FileStorage('/home/tumbochka/pokupki.txt')
item_list = ItemList.load(storage)
a = Item('apples', 'asdf', datetime.now(), 100)

start(item_list)
