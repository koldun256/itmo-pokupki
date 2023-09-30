from cli.command import Command
from cli.sanitize import sanitize_int

n_default = 10
def run_cost_command(args, item_list, descending=True):
    try:
        n = sanitize_int(args[0])
    except IndexError:
        n = n_default
    except ValueError:
        print('N должно быть целым положительным числом')
        return

    for item in sorted(
            item_list.get_items(),
            key=lambda item: item.cost,
            reverse=descending)[:n]:

        print(item.to_str())


cost_desc_command = Command(
    'Ц',
    f"Ц [N = {n_default}] - выводит N самых дорогих покупок",
    lambda args, item_list: run_cost_command(args, item_list, True)
)

cost_asc_command = Command(
    'ц',
    f"ц [N = {n_default}] - выводит N самых дешевых покупок",
    lambda args, item_list: run_cost_command(args, item_list, False)
)
