import pickle

def display_inventory():
    with open('inventory.pkl', 'rb') as f:
        data = pickle.load(f)
    laptops = data.get('laptops', [])
    
    
    # Print header
    print(f"{'ID':<8} {'Brand':<10} {'Model':<25} {'Processor':<25} {'RAM':<10} {'Storage':<12} {'OS':<8}")
    for laptop in laptops:
        id = laptop.get('id', '')
        brand = laptop.get('brand', '')
        model = laptop.get('model', '')
        processor = laptop.get('processor', '')
        ram_size = laptop.get('ram_gb', '')
        ram = f"{ram_size} GB" if ram_size else ""
        storage_size = laptop.get('storage-size_gb', '')
        storage = f"{storage_size} GB" if storage_size else ""
        os = "MacOS" if laptop.get('is_macos', False) else "Windows"
        
        
        print(
            f"{id:<8} "
            f"{brand:<10} "
            f"{model:<25} "
            f"{processor:<25} "
            f"{ram:<10} "
            f"{storage:<12} "
            f"{os:<8}"
        )

