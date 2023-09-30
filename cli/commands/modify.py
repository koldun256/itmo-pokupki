from cli.command import Command
from cli.questions import *
from cli.sanitize import sanitize_int


def get_item(args, item_list):
    id = args[0] \
        if len(args) >= 1 \
        else input('Введите ID покупки, которую хотите редактировать: ')

    try:
        return item_list.get_by_id(sanitize_int(id))
    except ValueError:
        print('ID должен быть целым положительным числом')
        return None
    except KeyError:
        print(f"Нет покупки с ID {id}")
        return None


def get_field_name(args):
    possible_names = ['н', 'к', 'д', 'ц']
    field_name = args[1] \
            if len(args) >= 2 \
            else input('Введите поле для редактирования (н, к, д, ц, о - отмена): ')

    if field_name in possible_names:
        return field_name
    elif field_name == 'о':
        return None
    else:
        print(f"Нет такого поля {field_name}")
        print('Доступные варианты: н - название, к - категория, д - дата, ц - цена')
        return None


def run_modify_command(args, item_list):
    item = get_item(args, item_list)
    if item is None:
        return
    print(f"Вы редактируете покупку \"{item.to_str()}\"")
    field_name = get_field_name(args)
    if field_name is None:
        return

    match field_name:
        case 'н': # modify name
            new_name = ask_name()
            if new_name is None:
                return
            item.name =  new_name
        case 'к': # modify category
            new_category = ask_category(item_list.get_categories())
            if new_category is None:
                return
            item.category = new_category
        case 'д': # modify date
            new_date = ask_date()
            if new_date is None:
                return
            item.date = new_date
        case 'ц': # modify cost
            new_cost = ask_cost()
            if new_cost is None:
                return
            item.cost = new_cost
    item_list.save()
    print(f"Покупка \"{item.to_str()}\" сохранена")


modify_command = Command(
    'р',
    'р [id] [поле] [значение] - редактирует покупку [id], изменяя значение в поле [поле]',
    run_modify_command
)

