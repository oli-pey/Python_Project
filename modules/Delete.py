import pickle
import os
import traceback
import modules.Display as Display


def delete_laptop():
    """
    Deletes a laptop from the inventory using its unique ID.
    """

    print("\n==============================")
    print("   CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    Display.display_inventory()

    print("\n==============================")
    print("   REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")

    # Ensure inventory file exists
    pickle_path = "data/test.pkl"
    if not os.path.exists(pickle_path):
        print("No inventory file found. Nothing to delete.")
        return

    # Load data safely (report the exception for debugging)
    try:
        with open(pickle_path, "rb") as f:
            data = pickle.load(f)
    except Exception as e:
        print(f"Error reading inventory file: {e}")
        traceback.print_exc()
        return

    laptops = data.get("laptops", [])

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
    with open(pickle_path, "wb") as f:
        pickle.dump(data, f)

    print(f"\nLaptop with ID '{laptop_id}' has been successfully removed.")
    print("Operation completed.\n")
