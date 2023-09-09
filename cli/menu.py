from cli.command import Command
def run_test(args, items):
    print('test!!!')
test_command = Command('test', 'asdf', run_test)
commands = [test_command]
def start(item_list):
    while True:
        command_text = input('Введите команду: ')
        if command_text == '':
            continue
        command_name, *args = command_text.split(' ')
        try:
            command = next(command for command in commands if command.name == command_name)
            command.run(args, item_list)
        except StopIteration:
            print(f"Нет команды {command_name}!")