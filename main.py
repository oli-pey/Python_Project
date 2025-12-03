from modules.Display import display_inventory
from modules.Create import create_laptop
from modules.Delete import delete_laptop
#from modules.Filter import filter_laptops
import time



def main():
    while True:
        print("Welcome to the Laptop Inventory Program")

        try:
            menuchoice = int(input(
                "If you want to display all devices, enter 1\n"
                "If you want to add a new device, enter 2\n"
                "If you want to delete a device, enter 3\n"
                "If you want to filter for specific devices, enter 4\n"
                "Your choice: "
            ))

            if menuchoice < 1 or menuchoice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
                time.sleep(2)
                continue  # restart the loop

        except ValueError:
            print("Invalid input. Please enter a number.")
            time.sleep(2)
            continue  # restart the loop

        # --- Valid choices ---
        if menuchoice == 1:
            print("Display all devices")
            display_inventory()
        elif menuchoice == 2:
            print("Add a new device")
            create_laptop()
        elif menuchoice == 3:
            print("Delete a device")
            delete_laptop()
        elif menuchoice == 4:
            print("Filter for specific devices")
            #filter_laptops()

        input("\nPress Enter to return to the main menu...")

if __name__ == '__main__':
    main()
