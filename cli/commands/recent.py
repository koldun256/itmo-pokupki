from cli.command import Command
from cli.sanitize import sanitize_int

n_default = 10
def run_recent_command(args, item_list):
    try:
        n = sanitize_int(args[0])
    except IndexError:
        n = n_default
    except ValueError:
        print('N должно быть целым положительным числом')
        return

    for item in sorted(
            item_list.get_items(),
            key=lambda item: item.date,
            reverse=True)[:n]:

        print(item.to_str())


recent_command = Command(
    'п',
    f"п [N = {n_default}] - выводит N последних покупок",
    run_recent_command
)

