"""
Laptop Inventory Program
Provides a menu interface to display, create, delete, and filter laptop entries
"""

# Import of modules (absolute imports are generally preferred)
from modules.display import display_inventory
from modules.create import create_laptop
from modules.delete import delete_laptop
from modules.filter import filter_laptops


def main():
    """Main program loop for user interaction."""
    while True:
        print("\nWelcome to the Laptop Inventory Program")

        try:
            menu_choice = int(
                input(
                    "If you want to display all devices, enter 1\n"
                    "If you want to add a new device, enter 2\n"
                    "If you want to delete a device, enter 3\n"
                    "If you want to filter for specific devices, enter 4\n"
                    "Your choice: "
                )
            )

            # Validate menu choice
            if menu_choice not in (1, 2, 3, 4):
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Execute the chosen action by calling the appropriate function
        if menu_choice == 1:
            print("\n--- Display all devices ---")
            display_inventory()

        elif menu_choice == 2:
            print("\n--- Add a new device ---")
            create_laptop()

        elif menu_choice == 3:
            print("\n--- Delete a device ---")
            delete_laptop()

        elif menu_choice == 4:
            print("\n--- Filter for specific devices ---")
            filter_laptops()


if __name__ == "__main__":
    main()
