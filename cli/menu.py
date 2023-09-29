from cli.command_router import process_command, UnknownCommandException

def start_cli(item_list):
    while True:
        command_text = input('Введите команду(с - справка): ')
        if command_text == '':
            continue

        try:
            process_command(command_text, item_list)
        except UnknownCommandException:
            print(f"Некорректная команда {command_text}!")
        except Exception:
             print(f"Неизвестная ошибка")

