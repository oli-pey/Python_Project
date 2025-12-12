from config.config import ALLOWED_BRANDS
from modules.Display import load_inventory, print_laptop_list


def print_results(laptops):
    """Prints the list of laptops that match the filter criteria."""
    if not laptops:
        print("No laptops match the filter criteria.")
        return
    print_laptop_list(laptops)

def get_numeric_input(prompt):
    """Prompts user for a numeric input until valid."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_brand_input():
    """Prompts user to select a valid brand."""
    allowed_upper = [b.upper() for b in ALLOWED_BRANDS]
    while True:
        print(f"Allowed Brands: {', '.join(ALLOWED_BRANDS)}")
        brand_choice = input("Brand: ").strip()
        if brand_choice.upper() in allowed_upper:
            return brand_choice
        print(f"Invalid brand. Please select from: {', '.join(ALLOWED_BRANDS)}")

def filter_laptops():
    """Provides a menu for filtering the laptop inventory by various criteria."""
    print("\n==============================")
    print("     FILTER LAPTOP INVENTORY")
    print("==============================\n")

    laptops = load_inventory()
    if not laptops:
        print("No laptops found in inventory.")
        return

    while True:
        menu = ("Filter by:\n"
                " 1) Minimum RAM (GB)\n"
                " 2) Minimum Storage (GB)\n"
                " 3) Brand\n"
                " 4) Minimum RAM AND Minimum Storage (GB)\n"
                " 5) Return to the main menu\n"
                "Your choice: ")

        try:
            choice = int(input(menu).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        results = []

        if choice == 1:  # Filter by RAM
            min_ram = get_numeric_input("Min RAM (GB): ")
            results = [l for l in laptops if int(l.get("ram_gb", 0)) >= min_ram]

        elif choice == 2:  # Filter by Storage
            min_storage = get_numeric_input("Min Storage (GB): ")
            results = [l for l in laptops if int(l.get("storage_gb", 0)) >= min_storage]

        elif choice == 3:  # Filter by Brand
            brand = get_brand_input()
            results = [l for l in laptops if l.get("brand", "").lower() == brand.lower()]

        elif choice == 4:  # Filter by RAM and Storage
            min_ram = get_numeric_input("Min RAM (GB): ")
            min_storage = get_numeric_input("Min Storage (GB): ")
            results = [l for l in laptops if int(l.get("ram_gb", 0)) >= min_ram and int(l.get("storage_gb", 0)) >= min_storage]

        elif choice == 5:  # Exit to main menu
            print("Returning to main menu.")
            return

        else:
            print("Invalid choice.")
            continue

        #Pass results to display function
        print_results(results)
        break
