# Import of modules (absolute imports are generally preferred)
from modules.Display import display_inventory
from modules.Create import create_laptop
from modules.Delete import delete_laptop
from modules.Filter import filter_laptops


def main():
    # Main program loop for user interaction
    while True:
        print("\nWelcome to the Laptop Inventory Program")
        
        try:
            menu_choice = int(input(
                "If you want to display all devices, enter 1\n"
                "If you want to add a new device, enter 2\n"
                "If you want to delete a device, enter 3\n"
                "If you want to filter for specific devices, enter 4\n"
                "Your choice: "
            ))
            
            # Validate menu choice
            if menu_choice < 1 or menu_choice > 4:
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
            
        # Instruct user to press Enter to return to main menu
        input("\nPress Enter to return to the main menu...")


if __name__ == '__main__':
    main()