import os
import pickle
PICKLE_PATH = 'data/test.pkl'

def display_inventory():
    laptops = []

    if os.path.exists(PICKLE_PATH):
        try:
            with open(PICKLE_PATH, 'rb') as f:
                data = pickle.load(f)
                laptops = data.get('laptops', [])
        except Exception:
            print("Error: Could not read inventory file.")
            laptops = []

    if not laptops:
        print("No laptops found in inventory.")
        return


    # Print header
    print(f"{'ID':<6} {'Brand':<12} {'Model':<25} {'Processor':<25} {'RAM':<10} {'Storage':<12} {'OS':<8}")
    print("-" * 100)

    # Print each laptop's details
    for laptop in laptops:
        laptop_id = laptop.get('id', '')
        brand = laptop.get('brand', '')
        model = laptop.get('model', '')
        processor = laptop.get('processor', '')
        ram = laptop.get('ram_gb')
        storage = laptop.get('storage_gb')
        os_name = 'MacOS' if laptop.get('is_macos', False) else 'Windows'

        ram_str = f"{ram} GB" if ram is not None and ram != '' else ''
        storage_str = f"{storage} GB" if storage is not None and storage != '' else ''

        print(f"{str(laptop_id):<6} {brand:<12} {model:<25} {processor:<25} {ram_str:<10} {storage_str:<12} {os_name:<8}")