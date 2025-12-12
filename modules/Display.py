import os
import pickle
from config.config import PICKLE_PATH


def display_inventory():
    "Loads and displays the current inventory of laptops."""
    laptops = load_inventory()
    if laptops:
        print_laptop_list(laptops)
        # Print if no error occurred during loading to notify empty inventory
    elif laptops is not None:  
        print("The inventory is currently empty.")


def load_inventory():
    """
    Loads laptop data from the pickle file specified by PICKLE_PATH.
    Returns a list of laptops or None if an error occurs.
    """
    # Initialize empty list
    laptops = []
    # File doesn't exist yet (e.g., first run), return empty list
    if not os.path.exists(PICKLE_PATH):
        return laptops

    try:
        with open(PICKLE_PATH, 'rb') as file:
            # Assuming the data is stored as a dictionary with a 'laptops' key
            data = pickle.load(file)
            laptops = data.get('laptops', []) 
    
    except (Exception):
        # Exception handling for file read/unpickle errors
        print(f"Critical Error: Could not read or unpickle inventory file at {PICKLE_PATH}.")
        return None
        
    return laptops


def print_laptop_list(laptops):
    """
    Prints the details of the given list of laptops in a formatted table.
    """
    # Print header (consistent column widths)
    print(f"{'ID':<6} {'Brand':<12} {'Model':<25} {'Processor':<25} {'RAM':<10} {'Storage':<12} {'OS':<8}")
    print("-" * 110)

    # Print each laptop's details
    for laptop in laptops:
        # Using variable names consistent with dictionary keys for readability
        laptop_id = laptop.get('id', '')
        brand = laptop.get('brand', '')
        model = laptop.get('model', '')
        processor = laptop.get('processor', '')

        ram_gb = laptop.get('ram_gb')
        storage_gb = laptop.get('storage_gb')
        
        # Format RAM and Storage, handling None values gracefully
        ram = f"{ram_gb} GB" if ram_gb is not None else ""
        storage = f"{storage_gb} GB" if storage_gb is not None else ""
        
        # Consistent variable naming
        os_name = "MacOS" if laptop.get('is_macos', False) else "Windows"

        print(f"{str(laptop_id):<6} {brand:<12} {model:<25} {processor:<25} {ram:<10} {storage:<12} {os_name:<8}")