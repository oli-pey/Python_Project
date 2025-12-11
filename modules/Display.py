import os
import pickle
from config.config import PICKLE_PATH

def display_inventory():
    laptops = load_inventory()
    if laptops:
        print_laptop_list(laptops)

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

def print_laptop_list(laptops):
    
    # Print header (consistent column widths)
    print(f"{"ID":<6} {"Brand":<12} {"Model":<25} {"Processor":<25} {"RAM":<10} {"Storage":<12} {"OS":<8}")
    print("-" * 100)

    # Print each laptop's details
    for laptop in laptops:
        laptop_id = laptop.get("id", "")
        brand = laptop.get("brand", "")
        model = laptop.get("model", "")
        processor = laptop.get("processor", "")

        ram_gb = laptop.get("ram_gb")
        storage_gb = laptop.get("storage_gb")
        
        # Format RAM and Storage, handling None values gracefully
        ram = f"{ram_gb} GB" if ram_gb is not None else ""
        storage = f"{storage_gb} GB" if storage_gb is not None else ""
        
        os_name = "MacOS" if laptop.get("is_macos", False) else "Windows"

        print(f"{str(laptop_id):<6} {brand:<12} {model:<25} {processor:<25} {ram:<10} {storage:<12} {os_name:<8}")