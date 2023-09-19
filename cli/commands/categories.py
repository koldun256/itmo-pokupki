def display_category(category, item_list):
    category_items = [item for item in item_list.items if item.category == category]
    total_cost = sum(item.cost for item in category_items)
    item_count = len(category_items)
    print(f"{category} ({item_count} | {total_cost})")
    for item in category_items:
        print(item.to_str())

def run_categories_command(args, item_list):
    category = ' '.join(args)
    
