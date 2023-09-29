from cli.command import Command

def list_by_cost(item_list, args, descending=True):
    for item in sorted(item_list.items,
                       key=lambda item: item.cost,
                       reverse=descending):
        print(item.to_str())


list_by_cost_descending_command = Command(
    'Ц',
    'Ц - вывести покупки, отсортированные по цене в порядке убывания',
    lambda item_list, args: list_by_cost(item_list, args, True)
)

list_by_cost_ascending_command = Command(
    'ц',
    'ц - вывести покупки, отсортированные по цене в порядке возрастания',
    lambda item_list, args: list_by_cost(item_list, args, False)
)
