import Create
import Display
import Delete


def Main():
    print("Welcome to the Laptop Inventory Programm")
    menuchoice = input("If you want to Display all Device enter 1 in the Console\n"
                           "If you want to add a new device enter 2\n"
                           "If you want to delete a device enter 3\n"
                           "Your choice: ")
    
    if menuchoice == "1":
            print("Display all devices")
            # Hier kann die Display-Funktion aufgerufen werden
            Display.display_inventory()
    elif menuchoice == "2":
            print("Add a new device")
            # Hier kann die Create-Funktion aufgerufen werden
            Create.create_laptop()
    elif menuchoice == "3":
            print("Delete a device")
            # Hier kann die Delete-Funktion aufgerufen werden
            Delete.delete_Laptop()
    else:
            print("Invalid choice")
            Main()

if __name__ == '__main__':
    Main()

