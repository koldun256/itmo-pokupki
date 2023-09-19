from data import *
from cli.menu import start

storage = FileStorage('/home/tumbochka/pokupki.txt')
item_list = ItemList.load(storage)

start(item_list)
