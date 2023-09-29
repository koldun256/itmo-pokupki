from data import FileStorage, ItemList
from cli.menu import start_cli
import os
import platform

if __name__ == '__main__':
    file_name = 'pokupki.txt'
    file_path = f"{os.getenv('HOME')}/{file_name}" \
                if platform.system() == 'Linux' \
                else f"{os.getenv('APPDATA')}\\{file_name}"

    storage = FileStorage(file_path)
    item_list = ItemList.load(storage)

    start_cli(item_list)
