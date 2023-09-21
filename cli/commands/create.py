from cli.item_form import get_name, get_category, get_date, get_cost
from data import Item
from cli.command import Command


def run_create_command(args, item_list):
    name = get_name()
    if name is None:
        return

    category = get_category(item_list.get_categories())
    if category is None:
        return

    date = get_date()
    if date is None:
        return

    cost = get_cost()
    if cost is None:
        return

    new_item = Item(name, category, date, cost)
    item_list.add(new_item)
    print(f"Покупка \"{new_item.to_str()}\" добавлена")


create_command = Command('н', 'н - новая покупка', run_create_command)

