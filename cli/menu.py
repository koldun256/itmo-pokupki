from cli.command import Command
from cli.create import create_command
from cli.recent import recent_command
from cli.exit import exit_command
from cli.delete import delete_command

commands = [create_command, recent_command, exit_command, delete_command]


def run_help(args, items):
    for command in commands:
        print(command.help)


help_command = Command('с', 'с - выводит эту справку', run_help)
commands.append(help_command)


def start(item_list):
    while True:
        command_text = input('Введите команду(с - справка): ')
        if command_text == '':
            continue
        command_name, *args = command_text.split(' ')
        try:
            command = next(cmd for cmd in commands if cmd.name == command_name)
            command.run(args, item_list)
        except StopIteration:
            print(f"Нет команды {command_name}!")

