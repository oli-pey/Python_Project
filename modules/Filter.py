from config.config import ALLOWED_BRANDS
from modules.Display import load_inventory, print_laptop_list


def print_results(laptops):
    """Prints the list of laptops that match the filter criteria."""
    if not laptops:
        print("No laptops match the filter criteria.")
        return

    print_laptop_list(laptops)


def filter_laptops():
    """Provides a menu for filtering the laptop inventory by various criteria."""
    
    print("\n==============================")
    print("     FILTER LAPTOP INVENTORY")
    print("==============================\n")

    laptops = load_inventory()
    if not laptops:
        print("No laptops found in inventory.")
        return

    # Print menu and get choice
    try:
        menu_choice = int(input(
                "If you want to display all devices, enter 1\n"
                "If you want to add a new device, enter 2\n"
                "If you want to delete a device, enter 3\n"
                "If you want to filter for specific devices, enter 4\n"
                "If you want to return to the main menu, enter 5\n"
                "Your choice: "
            ))
    
    
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    results = []

    # 1. Filter by Minimum RAM
    if menu_choice == 1:
        try:
            min_ram = int(input("Min RAM (GB): ").strip())
            results = [l for l in laptops if int(l.get("ram_gb", 0)) >= min_ram]
        except ValueError:
            print("Invalid input. Please enter a numeric RAM value.")
            return

    # 2. Filter by Minimum Storage
    elif menu_choice == 2:
        try:
            min_storage = int(input("Min Storage (GB): ").strip())
            results = [l for l in laptops if int(l.get("storage_gb", 0)) >= min_storage]
        except ValueError:
            print("Invalid input. Please enter a numeric storage value.")
            return

    # 3. Filter by Brand (Corrected choice number from 4 to 3)
    elif menu_choice == 3:
        # PEP 8 spacing around the join method
        print(f"Allowed Brands: {', '.join(ALLOWED_BRANDS)}")
        brand_choice = input("Brand: ").strip()
        
        if brand_choice.upper() not in [b.upper() for b in ALLOWED_BRANDS]:
            print(f"Invalid brand. Please select from: {', '.join(ALLOWED_BRANDS)}")
            return
            
        results = [l for l in laptops if l.get("brand", "").lower() == brand_choice.lower()]

    # 4. Filter by Min RAM AND Min Storage (Corrected choice number from 5 to 4)
    elif menu_choice == 4:
        try:
            min_ram = int(input("Min RAM (GB): ").strip())
            min_storage = int(input("Min Storage (GB): ").strip())
            
            # Improved readability for the list comprehension over multiple lines
            results = [
                l for l in laptops 
                if int(l.get("ram_gb", 0)) >= min_ram 
                and int(l.get("storage_gb", 0)) >= min_storage
            ]
        except ValueError:
            print("Invalid input. Please enter numeric values for both RAM and Storage.")
            return
        
    # 5. Return to Main Menu
    elif menu_choice == 5:
        print("Returning to main menu.")
        return

    else:
        print("Invalid choice.")
        return

    print_results(results)