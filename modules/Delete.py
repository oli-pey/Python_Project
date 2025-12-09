import pickle
import os
import modules.Display as Display

def delete_laptop():
    print("\n==============================")
    print("   CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    
    Display.display_inventory()

    print("\n==============================")
    print("   REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")

    pickle_path = "data/inventory.pkl"

    # ---------------------------------------------------------
    #  UPDATED LOADING LOGIC
    # ---------------------------------------------------------
    # Initialize defaults so 'data' exists even if loading fails
    data = {"laptops": []}
    laptops = []

    if os.path.exists(pickle_path):
        try:
            with open(pickle_path, 'rb') as f:
                data = pickle.load(f)
                # Use .get() to avoid errors if the 'laptops' key is missing inside the file
                laptops = data.get('laptops', []) 
        except Exception:
            # Handle corrupted files or read errors safely
            print("Warning: Could not read inventory file. Starting with empty inventory.")
            data = {"laptops": []}
            laptops = []
    # ---------------------------------------------------------

    # Check if we actually have laptops to delete to avoid an infinite loop below
    if not laptops:
        print("Inventory is empty or file not found. Nothing to delete.")
        return

    # Build list of IDs in inventory
    existing_ids = [laptop.get("id") for laptop in laptops]

    # Request a valid numeric ID
    while True:
        user_input = input("Please enter the Laptop ID to remove: ").strip()

        if not user_input.isdigit():
            print("Laptop ID must be numeric.")
            continue

        laptop_id = int(user_input)

        if laptop_id not in existing_ids:
            print(f"No laptop found with ID '{laptop_id}'. Please try again.")
            continue

        break  # valid ID found

    # Remove the selected laptop
    data["laptops"] = [
        laptop for laptop in laptops if laptop.get("id") != laptop_id
    ]

    # Save updated inventory
    try:
        with open(pickle_path, "wb") as f:
            pickle.dump(data, f)
        print(f"\nLaptop with ID '{laptop_id}' has been successfully removed.")
        print("Operation completed.\n")
    except Exception as e:
        print(f"Error saving changes: {e}")