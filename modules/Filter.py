from config.config import ALLOWED_BRANDS
from modules.Display import load_inventory




def print_results(laptops):
    if not laptops:
        print("No laptops match the filter criteria.")
        return

    print(f"Found {len(laptops)} matching laptop(s):")
    print(f"{"ID":<6} {"Brand":<12} {"Model":<25} {"RAM":<8} {"Storage":<10} {"OS":<8}")
    print("-" * 70)
    for l in laptops:
        laptop_id = l.get("id", "")
        brand = l.get("brand", "")
        model = l.get("model", "")
        ram = f"{l.get("ram_gb", "")} GB" if l.get("ram_gb") is not None else ""
        storage = f"{l.get("storage_gb", "")} GB" if l.get("storage_gb") is not None else ""
        os_name = "MacOS" if l.get("is_macos", False) else "Windows"
        print(f"{str(laptop_id):<6} {brand:<12} {model:<25} {ram:<8} {storage:<10} {os_name:<8}")


def filter_laptops():
    
    print("\n==============================")
    print("   FILTER LAPTOP INVENTORY")
    print("==============================\n")

    laptops = load_inventory()
    if not laptops:
        print("No laptops found in inventory.")
        return

    # Print menu and get choice
    print("\nFilter by:")
    print(" 1) Minimum RAM (GB)")
    print(" 2) Minimum Storage (GB)")
    print(" 3) Brand")
    print(" 4) Min RAM AND Min Storage (GB)")
    menuchoice = int(input("Your choice: "))

    results = []

    # 1. Filter by Minimum RAM (example minimum 32 GB input works here)
    if menuchoice == 1:
        try:
            min_ram = int(input("Min RAM (GB): ").strip())
            results = [l for l in laptops if int(l.get("ram_gb", 0)) >= min_ram]
        except ValueError:
            print("Invalid input. Please enter a numeric RAM value.")
            return

    # 2. Filter by Minimum Storage
    elif menuchoice == 2:
        try:
            min_storage = int(input("Min Storage (GB): ").strip())
            results = [l for l in laptops if int(l.get("storage_gb", 0)) >= min_storage]
        except ValueError:
            print("Invalid input. Please enter a numeric storage value.")
            return


    # 4. Filter by Brand
    elif menuchoice == 3:
        print(f"Allowed Brands: {", ".join(ALLOWED_BRANDS)}")
        brand_choice = input("Brand: ").strip()
        if brand_choice not in ALLOWED_BRANDS:
            print(f"Invalid brand. Please select from: {", ".join(ALLOWED_BRANDS)}")
            return
        results = [l for l in laptops if l.get("brand", "").lower() == brand_choice.lower()]

    # 5. Filter by Min RAM AND Min Storage
    elif menuchoice == 4:
        try:
            min_ram = int(input("Min RAM (GB): ").strip())
            min_storage = int(input("Min Storage (GB): ").strip())
            results = [
                l for l in laptops 
                if int(l.get("ram_gb", 0)) >= min_ram and int(l.get("storage_gb", 0)) >= min_storage
            ]
        except ValueError:
            print("Invalid input. Please enter numeric values for both RAM and Storage.")
            return

    else:
        print("Invalid choice.")
        return

    print_results(results)