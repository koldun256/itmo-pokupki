from cli.command import Command
from cli.sanitize import sanitize_date
from datetime import date
def display_date(date, item_list):
    date_items = [
        item
        for item
        in item_list.items
        if item.date.date() == date
    ]
    total_cost = sum(item.cost for item in date_items)
    item_count = len(date_items)
    print(f"{date.strftime('%d.%m.%y')} ({item_count} | {total_cost}):")
    for item in date_items:
        print(item.to_str())


def run_date_command(args, item_list):
    try:
        date = sanitize_date(args[0]).date() if len(args) >= 1 else None
    except ValueError:
        print('Неверная дата')
        return
    dates = {item.date.date() for item in item_list.items}
    if date is None:
        for date in dates:
            display_date(date, item_list)
        return
    
    display_date(date, item_list)


date_command = Command(
    'д',
    'д [дата = все] - вывести покупки в определенную дату',
    run_date_command
)
