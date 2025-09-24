import json

def display_inventory():
    with open('inventory.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    laptops = data.get('laptops', [])
    # Print header
    print(f"{'ID':<8} {'Brand':<10} {'Model':<25} {'Processor':<25} {'RAM':<5} {'Storage':<12} ")
    for laptop in laptops:
        storage = laptop.get('storage', {})
        storage_type = str(storage.get('type', '') or '')
        storage_capacity = str(storage.get('capacity_gb', '') or '')
        storage_str = f"{storage_type} {storage_capacity}GB"
        print(
            f"{str(laptop.get('id', '') or ''):<8} "
            f"{str(laptop.get('brand', '') or ''):<10} "
            f"{str(laptop.get('model', '') or ''):<25} "
            f"{str(laptop.get('processor', '') or ''):<25} "
            f"{str(laptop.get('ram_gb', '') or ''):<5} "
            f"{storage_str:<12} "
        )

if __name__ == '__main__':
    display_inventory()