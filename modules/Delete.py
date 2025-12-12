import pickle
from modules.Display import display_inventory, load_inventory 
from config.config import PICKLE_PATH


def delete_laptop():
    """Handles the user interaction for deleting a laptop entry from the inventory."""
    print("\n==============================")
    print("     CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    
    # Display current inventory for user reference
    laptops = load_inventory()
    if not laptops:
        print("Inventory is empty. Nothing to delete.")
        return
    else:   
        display_inventory()

    print("\n==============================")
    print("     REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")

    # Normalize IDs to Strings for comparison (ensuring consistency with user input)
    # Using 'str()' handles cases where IDs might be stored as int or str
    existing_ids = [str(laptop.get("id")) for laptop in laptops]

    while True:
        user_input = input("Enter the Laptop ID to remove: ").strip()
        if user_input.lower() in ["back", "exit"]:
            print("Returning to main menu.")
            return
        if not user_input.isdigit():
            print("Laptop ID must be numeric. Try again.")
            continue
        if user_input not in existing_ids:
            print(f"No laptop found with ID '{user_input}'. Please try again.")
            continue
        laptop_id_to_remove = user_input
        break

    # Robust Deletion Logic: Creates a new list excluding the item with the matching ID
    new_laptop_list = [
        laptop for laptop in laptops 
        if str(laptop.get("id")) != laptop_id_to_remove
    ]
    
    # Prepare data dictionary for saving
    data_to_save = {"laptops": new_laptop_list}

    # Save updated inventory
    try:
        with open(PICKLE_PATH, "wb") as pickle_file:
            pickle.dump(data_to_save, pickle_file)
            
        print(f"\nLaptop with ID '{laptop_id_to_remove}' has been successfully removed.")
        print("Operation completed.\n")
        
    except Exception as e:
        print(f"Error saving changes: {e}")

        