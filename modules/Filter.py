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

    results = []
    
    # Filter loop starts here, repeats until a filter is applied or user exits
    while True:
        # Print menu and get choice
        menu = (
            "Filter by:\n"
            " 1) Minimum RAM (GB)\n"
            " 2) Minimum Storage (GB)\n"
            " 3) Brand\n"
            " 4) Minimum RAM AND Minimum Storage (GB)\n"
            " 5) Return to the main menu\n"
            "Your choice: "
        )

        try:
            menu_choice = int(input(menu).strip())
        
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue # Restart the while loop (re-show menu)

        # 1. Filter by Minimum RAM
        if menu_choice == 1:
            try:
                min_ram = int(input("Min RAM (GB): ").strip())
                results = [l for l in laptops if int(l.get("ram_gb", 0)) >= min_ram]
                break # Exit loop to print results
            except ValueError:
                print("Invalid input. Please enter a numeric RAM value.")
                continue # Restart the while loop

        # 2. Filter by Minimum Storage
        elif menu_choice == 2:
            try:
                min_storage = int(input("Min Storage (GB): ").strip())
                results = [l for l in laptops if int(l.get("storage_gb", 0)) >= min_storage]
                break # Exit loop to print results
            except ValueError:
                print("Invalid input. Please enter a numeric storage value.")
                continue # Restart the while loop

        # 3. Filter by Brand
        elif menu_choice == 3:
            print(f"Allowed Brands: {', '.join(ALLOWED_BRANDS)}")
            brand_choice = input("Brand: ").strip()
            
            # Consistent case-insensitive validation
            if brand_choice.upper() not in [b.upper() for b in ALLOWED_BRANDS]:
                print(f"Invalid brand. Please select from: {', '.join(ALLOWED_BRANDS)}")
                continue # Restart the while loop
                
            results = [l for l in laptops if l.get("brand", "").lower() == brand_choice.lower()]
            break # Exit loop to print results

        # 4. Filter by Min RAM AND Min Storage
        elif menu_choice == 4:
            try:
                min_ram = int(input("Min RAM (GB): ").strip())
                min_storage = int(input("Min Storage (GB): ").strip())
                
                results = [
                    l for l in laptops 
                    if int(l.get("ram_gb", 0)) >= min_ram 
                    and int(l.get("storage_gb", 0)) >= min_storage
                ]
                break # Exit loop to print results
            except ValueError:
                print("Invalid input. Please enter numeric values for both RAM and Storage.")
                continue # Restart the while loop
            
        # 5. Return to Main Menu - Exit logic is clean
        elif menu_choice == 5:
            print("Returning to main menu.")
            return # Exit the function entirely
        
        # Handle all other invalid numerical choices
        else:
            print("Invalid choice.")
            continue # Restart the while loop (re-show menu)

    # This line is only reached if a filter was successfully applied (break was hit)
    print_results(results)