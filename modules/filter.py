from modules.display import print_laptop_list
from modules.display import load_inventory
from config.config import ALLOWED_BRANDS

def print_results(laptops):
    """Print the list of laptops matching the filter criteria."""
    if not laptops:
        print("No laptops match the filter criteria.")
        return

    print_laptop_list(laptops)


def get_numeric_input(prompt):
    """Prompt the user for a numeric input until valid and return it."""
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_brand_input():
    """Prompt the user to select a valid brand from ALLOWED_BRANDS."""
    allowed_upper = [
        brand.upper()
        for brand in ALLOWED_BRANDS
    ]

    while True:
        print(f"Allowed Brands: {', '.join(ALLOWED_BRANDS)}")
        brand_choice = input("Brand: ").strip()

        if brand_choice.upper() in allowed_upper:
            return brand_choice

        print(
            "Invalid brand. Please select from: "
            f"{', '.join(ALLOWED_BRANDS)}"
        )


def filter_laptops():
    """
    Provide a menu for filtering the laptop inventory by various criteria.
    """
    print("\n======================================================")
    print("              FILTER LAPTOP INVENTORY")
    print("To exit filtering, enter 'back' or 'exit' at any time")
    print("======================================================\n")

    laptops = load_inventory()
    if not laptops:
        print("No laptops found in inventory.")
        return

    while True:
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
            choice = int(input(menu).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        results = []

        if choice == 1:
            min_ram = get_numeric_input("Min RAM (GB): ")
            results = [
                laptop for laptop in laptops
                if int(laptop.get("ram_gb", 0)) >= min_ram
            ]

        elif choice == 2:
            min_storage = get_numeric_input("Min Storage (GB): ")
            results = [
                laptop for laptop in laptops
                if int(laptop.get("storage_gb", 0)) >= min_storage
            ]

        elif choice == 3:
            brand = get_brand_input()
            results = [
                laptop for laptop in laptops
                if laptop.get("brand", "").lower() == brand.lower()
            ]

        elif choice == 4:
            min_ram = get_numeric_input("Min RAM (GB): ")
            min_storage = get_numeric_input("Min Storage (GB): ")
            results = [
                laptop for laptop in laptops
                if (
                    int(laptop.get("ram_gb", 0)) >= min_ram
                    and int(laptop.get("storage_gb", 0)) >= min_storage
                )
            ]

        elif choice == 5:
            print("Returning to main menu.")
            return

        else:
            print("Invalid choice.")
            continue

        print_results(results)
        break
