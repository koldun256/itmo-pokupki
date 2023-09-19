from cli.command import Command


def display_category(category, item_list):
    category_items = [
        item
        for item
        in item_list.items
        if item.category == category
    ]
    total_cost = sum(item.cost for item in category_items)
    item_count = len(category_items)
    print(f"{category} ({item_count} | {total_cost})")
    for item in category_items:
        print(item.to_str())


def run_categories_command(args, item_list):
    category = ' '.join(args).strip()
    categories = item_list.get_categories()

    if category == '':
        for category in categories:
            display_category(category, item_list)
        return

    if category not in categories:
        print(f"Нет такой категории {category}")
        print(f"Список доступных категорий: {' | '.join(categories)}")
        return

    display_category(category, item_list)


category_command = Command(
    'к',
    'к [категория = все] - выводит информацию о покупках в категории',
    run_categories_command
)
