from cli.command import Command
from cli.create import create_command
commands = [create_command]
def run_help(args, items):
    for command in commands:
        print(f"{command.name} - {command.help}")
help_command = Command('с', 'выводит это сообщение', run_help)
commands.append(help_command)
def start(item_list):
    while True:
        command_text = input('Введите команду(с - справка): ')
        if command_text == '':
            continue
        command_name, *args = command_text.split(' ')
        try:
            command = next(command for command in commands if command.name == command_name)
            command.run(args, item_list)
        except StopIteration:
            print(f"Нет команды {command_name}!")