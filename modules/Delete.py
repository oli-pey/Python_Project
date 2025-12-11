import pickle
from modules.Display import display_inventory, load_inventory 
from config.config import PICKLE_PATH


def delete_laptop():
    """Handles the user interaction for deleting a laptop entry from the inventory."""
    print("\n==============================")
    print("     CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    
    # Display current inventory for user reference
    display_inventory()

    print("\n==============================")
    print("     REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")
    
    # Use load_inventory to handle reading data and error checks
    laptops = load_inventory()

    if not laptops:
        print("Inventory is empty. Nothing to delete.")
        return

    # Normalize IDs to Strings for comparison (ensuring consistency with user input)
    # Using 'str()' handles cases where IDs might be stored as int or str
    existing_ids = [str(laptop.get("id")) for laptop in laptops]

    laptop_id_to_remove = None
    while True:
        user_input = input("Please enter the Laptop ID to remove: ").strip()

        # Check if ID exists (comparing strings)
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
        # Use 'file' instead of 'f' for better clarity
        with open(PICKLE_PATH, "wb") as file:
            pickle.dump(data_to_save, file)
            
        print(f"\nLaptop with ID '{laptop_id_to_remove}' has been successfully removed.")
        print("Operation completed.\n")
        
    except Exception as e:
        # Catch and print the specific error for better diagnostics
        print(f"Error saving changes: {e}")