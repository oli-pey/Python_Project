import os
import pickle
from config.config import PICKLE_PATH

def load_inventory():
        laptops = []

        if os.path.exists(PICKLE_PATH):
            try:
                with open(PICKLE_PATH, "rb") as f:
                    data = pickle.load(f)
                    # Use .get() to avoid errors if the "laptops" key is missing inside the file
                    laptops = data.get("laptops", []) 
            except Exception:
                # Handle corrupted files or read errors safely
                print("Warning: Could not read inventory file")
                exit()
        return laptops

def display_inventory():
    
    laptops = load_inventory()
    # Print header
    print(f"{"ID":<6} {"Brand":<12} {"Model":<25} {"Processor":<25} {"RAM":<10} {"Storage":<12} {"OS":<8}")
    print("-" * 100)

    # Print each laptop"s details
    for laptop in laptops:
        laptop_id = laptop.get("id", "")
        brand = laptop.get("brand", "")
        model = laptop.get("model", "")
        processor = laptop.get("processor", "")
        ram = str(laptop.get("ram_gb", "")) + " GB"
        storage = str(laptop.get("storage_gb", "")) + " GB"
        os_name = "MacOS" if laptop.get("is_macos", False) else "Windows"

        print(f"{str(laptop_id):<6} {brand:<12} {model:<25} {processor:<25} {ram:<10} {storage:<12} {os_name:<8}")