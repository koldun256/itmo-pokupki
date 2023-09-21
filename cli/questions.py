from cli.sanitize import *
from datetime import datetime

def ask_name():
    user_input = input('Введите название покупки(о - отмена): ')
    if user_input == 'о':
        return None
    try:
        return sanitize_str(user_input)
    except ValueError:  # try again
        return ask_name()


def ask_category(categories):
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
                return ask_category(categories)
    except ValueError:  # try again
        return ask_category(categories)


def ask_date():
    user_input = input('Введите дату покупки (пустой ввод - сегодня, о - отмена): ')
    if user_input == 'о':
        return None
    if user_input == '':
        return datetime.now()
    try:
        return sanitize_date(user_input)
    except ValueError:  # try again
        return ask_date()


def ask_cost():
    user_input = input('Введите стоимость покупки (о - отмена): ')
    if user_input == 'о':
        return None

    try:
        return sanitize_int(user_input)
    except ValueError:  # try again
        return ask_cost()

