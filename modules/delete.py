import pickle
from modules.display import display_inventory
from modules.display import load_inventory
from config.config import PICKLE_PATH


def delete_laptop():
    """Handle user input for deleting a laptop entry from the inventory."""
    print("\n==============================")
    print("     CURRENT LAPTOP INVENTORY")
    print("==============================\n")

    laptops = load_inventory()

    if not laptops:
        print("Inventory is empty. Nothing to delete.")
        return

    display_inventory()

    print("\n====================================================")
    print("           REMOVE LAPTOP FROM INVENTORY")
    print("To exit deletion, enter 'back' or 'exit' at any time")
    print("====================================================\n")

    existing_ids = [laptop.get("id") for laptop in laptops]

    while True:
        user_input = input("Enter the Laptop ID to remove: ").strip()

        if user_input.lower() in ("back", "exit"):
            print("Returning to main menu.")
            return

        if not user_input.isdigit():
            print("Laptop ID must be numeric. Try again.")
            continue

        laptop_id_to_remove = int(user_input)

        if laptop_id_to_remove not in existing_ids:
            print(f"No laptop found with ID '{user_input}'. Please try again.")
            continue

        break

    # Create new list excluding the laptop with matching ID
    new_laptop_list = [
        laptop for laptop in laptops
        if laptop.get("id") != laptop_id_to_remove
    ]

    data_to_save = {"laptops": new_laptop_list}

    try:
        with open(PICKLE_PATH, "wb") as pickle_file:
            pickle.dump(data_to_save, pickle_file)

        print(
            f"\nLaptop with ID '{laptop_id_to_remove}' "
            "has been successfully removed."
        )
        print("Operation completed.\n")

    except Exception as exc:
        print(f"Error saving changes: {exc}")
