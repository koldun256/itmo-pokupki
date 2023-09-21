from cli.questions import *
from data import Item
from cli.command import Command


def run_create_command(args, item_list):
    name = ask_name()
    if name is None:
        return

    category = ask_category(item_list.get_categories())
    if category is None:
        return

    date = ask_date()
    if date is None:
        return

    cost = ask_cost()
    if cost is None:
        return

    new_item = Item(name, category, date, cost)
    item_list.add(new_item)
    print(f"Покупка \"{new_item.to_str()}\" добавлена")


create_command = Command('н', 'н - новая покупка', run_create_command)

