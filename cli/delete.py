from cli.command import Command
from cli.sanitize import sanitize_bool
def run_delete_command(args, item_list):
    id_str = args[0] if len(args) > 0 else input('Введите ID покупки, которую хотите удалить(о - отмена): ')
    if id_str in ('', 'о'):
        return

    try:
        item_id = int(id_str)
        if item_id <= 0:
            raise ValueError
    except ValueError:
        print('Неверный ID покупки')
        return
    
    try:
        item = item_list.get_by_id(item_id)
    except StopIteration:
        print('Нет покупки с таким ID')
        return
    
    confirmation_input = input(f"Вы точно хотите удалить покупку \"{item.to_str()}\" (Д/н)?: ")
    try:
        should_delete = sanitize_bool(confirmation_input, default = True)
    except ValueError:
        return
    
    if should_delete:
        item_list.delete(item_id)
        print(f"Покупка \"{item.to_str()}\" удалена")

delete_command = Command('у', 'у [ID] - удалить покупку с заданым ID', run_delete_command)