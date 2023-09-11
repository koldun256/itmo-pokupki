from cli.command import Command
def run_recent_command(args, item_list):
    try:
        n = int(args[0])
        if n <= 0:
            raise ValueError
    except ValueError:
        print('N должно быть целым положительным числом')
    except IndexError:
        n = 10
    
    for item in sorted(item_list.items, key = lambda item: item.date, reverse = True)[:n]:
        print(item.to_str())

recent_command = Command('п', 'п [N = 10] - выводит N последних покупок', run_recent_command)