from cli.sanitize import sanitize_str, sanitize_int, sanitize_date, sanitize_bool
from data import Item
from cli.command import Command
from datetime import datetime


def get_name():
    user_input = input('Введите название покупки(о - отмена): ')
    if user_input == 'о':
        return None
    try:
        return sanitize_str(user_input)
    except ValueError:  # try again
        return get_name()


def get_category(categories):
    user_input = input('Введите категорию покупки(о - отмена): ')
    if user_input == 'о':
        return None
    try:
        category = sanitize_str(user_input)
        if category in categories:
            return category
        else:
            print(f"Нет такой категории {category}")
            print(f"Существующие категории: {' | '.join(categories)}")
            should_create = None
            while should_create is None:
                user_input = input(f"Создать категорию {category} (Д/н)?: ")
                try:
                    should_create = sanitize_bool(user_input, default=True)
                except ValueError:
                    should_create = None

            if should_create:
                return category
            else:  # try again
                return get_category(categories)
        return sanitize_str(user_input)
    except ValueError:  # try again
        return get_category(categories)


def get_date():
    user_input = input('Введите дату покупки (пустой ввод - сегодня, о - отмена): ')
    if user_input == 'о':
        return None
    if user_input == '':
        return datetime.now()
    try:
        return sanitize_date(user_input)
    except ValueError:  # try again
        return get_date()


def get_cost():
    user_input = input('Введите стоимость покупки (о - отмена): ')
    if user_input == 'о':
        return None

    try:
        return sanitize_int(user_input)
    except ValueError:  # try again
        return get_cost()


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

