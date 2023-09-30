from cli.command import Command
from cli.commands.create import create_command
from cli.commands.recent import recent_command
from cli.commands.exit import exit_command
from cli.commands.delete import delete_command
from cli.commands.categories import category_command
from cli.commands.modify import modify_command
from cli.commands.date import date_command
from cli.commands.cost import cost_desc_command, cost_asc_command

commands = [
    create_command,
    modify_command,
    delete_command,
    recent_command,
    cost_desc_command,
    cost_asc_command,
    date_command,
    category_command,
    exit_command,
]


def run_help(args, item_list):
    for command in commands:
        print(command.help)


help_command = Command('с', 'с - выводит эту справку', run_help)
commands.append(help_command)


class UnknownCommandException(Exception):
    pass


def process_command(command_text, item_list):
    command_name, *args = command_text.split(' ')
    try:
        command = next(cmd for cmd in commands if cmd.name == command_name)
        command.run(args, item_list)
    except StopIteration:
        raise UnknownCommandException
