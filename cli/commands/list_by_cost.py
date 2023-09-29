from cli.command import Command

def list_by_cost(args, item_list, descending=True):
    for item in sorted(item_list.get_items(),
                       key=lambda item: item.cost,
                       reverse=descending):
        print(item.to_str())


list_by_cost_descending_command = Command(
    'Ц',
    'Ц - вывести покупки, отсортированные по цене в порядке убывания',
    lambda args, item_list: list_by_cost(args, item_list, True)
)

list_by_cost_ascending_command = Command(
    'ц',
    'ц - вывести покупки, отсортированные по цене в порядке возрастания',
    lambda args, item_list: list_by_cost(args, item_list, False)
)
