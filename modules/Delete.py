import pickle
import os
from modules.Display import display_inventory
from config.config import PICKLE_PATH

def delete_laptop():
    print("\n==============================")
    print("   CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    
    display_inventory()

    print("\n==============================")
    print("   REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")
    
    # --- FIX 1: Initialize 'data' early to prevent scope errors ---
    data = {"laptops": []} 
    laptops = []

    if os.path.exists(PICKLE_PATH):
        try:
            with open(PICKLE_PATH, 'rb') as f:
                data = pickle.load(f)
                laptops = data.get('laptops', []) 
        except Exception:
            print("Warning: Could not read inventory file")
            exit()

    if not laptops:
        print("Inventory is empty or file not found. Nothing to delete.")
        return

    # --- FIX 2: Normalize IDs to Strings for comparison ---
    # We convert existing IDs to strings to ensure we can match input regardless of stored type
    existing_ids = [str(laptop.get("id")) for laptop in laptops]

    while True:
        user_input = input("Please enter the Laptop ID to remove: ").strip()

        # Check if ID exists (comparing strings)
        if user_input not in existing_ids:
            print(f"No laptop found with ID '{user_input}'. Please try again.")
            continue

        laptop_id_to_remove = user_input
        break 

    # --- FIX 3: Robust Deletion Logic ---
    # Convert both the stored ID and target ID to strings during comparison
    # This ensures 1 matches "1"
    new_laptop_list = [
        laptop for laptop in laptops 
        if str(laptop.get("id")) != str(laptop_id_to_remove)
    ]
    
    # Update data dictionary
    data["laptops"] = new_laptop_list

    # Save updated inventory
    try:
        with open(PICKLE_PATH, "wb") as f:
            pickle.dump(data, f)
        print(f"\nLaptop with ID '{laptop_id_to_remove}' has been successfully removed.")
        print("Operation completed.\n")
    except Exception as e:
        print(f"Error saving changes: {e}")