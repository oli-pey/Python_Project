import pickle
from modules.display import load_inventory
from config.config import PICKLE_PATH
from config.config import ALLOWED_BRANDS
from config.config import ALLOWED_PROCESSORS


def create_laptop():
    """
    Handle user interaction for creating a new laptop entry
    and saving it to the inventory.
    """
    print("\n==============================")
    print("     ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")

    laptops = load_inventory()
    if laptops is None:
        print("Could not load inventory. Aborting.")
        return

    existing_ids = [laptop.get("id") for laptop in laptops]

    # -------------------------
    #   INPUT VALIDATION
    # -------------------------

    def laptop_id_input():
        """Prompt and validate a unique, 4-digit numeric laptop ID."""
        while True:
            laptop_id_str = input("Enter laptop ID (4 digits): ").strip()

            if laptop_id_str.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if not laptop_id_str:
                print("Laptop ID cannot be empty.")
                continue

            if not laptop_id_str.isdigit():
                print("Laptop ID must be numeric.")
                continue

            if len(laptop_id_str) != 4:
                print("Laptop ID must be exactly 4 digits.")
                continue

            laptop_id = int(laptop_id_str)
            if laptop_id in existing_ids:
                print(f"Laptop ID {laptop_id} already exists. Choose another.")
                continue
            return laptop_id

    def brand_input():
        """Prompt and validate a brand from ALLOWED_BRANDS."""
        print(f"Allowed Brands: {', '.join(ALLOWED_BRANDS)}")

        while True:
            brand = input("Enter laptop manufacturer: ").strip()

            if brand.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if not brand:
                print("Brand cannot be empty.")
                continue

            brand_title = brand.title()
            if brand_title not in ALLOWED_BRANDS:
                print(f"Invalid brand. Allowed: {', '.join(ALLOWED_BRANDS)}")
                continue
            return brand_title

    def model_input():
        """Prompt and validate a non-empty laptop model (max 25 chars)."""
        while True:
            model = input("Enter laptop model: ").strip()

            if model.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if not model:
                print("Model cannot be empty.")
                continue

            if len(model) > 25:
                print("Model name too long (max 25 characters).")
                continue
            return model

    def processor_input():
        """Prompt and validate a processor from ALLOWED_PROCESSORS."""
        print(f"Allowed Processors: {', '.join(ALLOWED_PROCESSORS)}")

        while True:
            processor = input("Enter processor: ").strip()

            if processor.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if processor not in ALLOWED_PROCESSORS:
                print("Invalid processor. Choose from the allowed list.")
                continue
            return processor

    def ram_input():
        """Prompt and validate RAM (8–256 GB, multiple of 8)."""
        while True:
            ram_value = input("Enter RAM in GB: ").strip()

            if ram_value.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if not ram_value.isdigit():
                print("Please enter a numeric value.")
                continue

            ram_gb = int(ram_value)

            if not (8 <= ram_gb <= 256):
                print("RAM must be between 8GB and 256GB.")
                continue

            if ram_gb % 8 != 0:
                print("RAM must be a multiple of 8GB.")
                continue
            return ram_gb

    def storage_input():
        """Prompt and validate storage (256–2048 GB, multiple of 256)."""
        while True:
            storage_value = input("Enter storage in GB: ").strip()

            if storage_value.lower() in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if not storage_value.isdigit():
                print("Please enter a numeric value.")
                continue

            storage_gb = int(storage_value)

            if not (256 <= storage_gb <= 2048):
                print("Storage must be between 256GB and 2048GB.")
                continue

            if storage_gb % 256 != 0:
                print("Storage must be a multiple of 256GB.")
                continue
            return storage_gb

    def os_input():
        """Prompt and validate OS (Windows/macOS). Return boolean for macOS."""
        while True:
            os_name = input("Enter OS (Windows/macOS): ").strip().lower()

            if os_name in ("back", "exit"):
                print("Returning to main menu.")
                return None

            if os_name == "macos":
                return True

            if os_name == "windows":
                return False
            print("Invalid input. Enter Windows or macOS.")

    # -------------------------
    #   COLLECT USER INPUT
    # -------------------------

    laptop_id = laptop_id_input()
    if laptop_id is None:
        return

    brand = brand_input()
    if brand is None:
        return

    model = model_input()
    if model is None:
        return

    processor = processor_input()
    if processor is None:
        return

    ram_gb = ram_input()
    if ram_gb is None:
        return

    storage_gb = storage_input()
    if storage_gb is None:
        return

    is_macos = os_input()
    if is_macos is None:
        return

    # -------------------------
    #   SAVE NEW LAPTOP
    # -------------------------

    laptop = {
        "id": laptop_id,
        "brand": brand,
        "model": model,
        "processor": processor,
        "ram_gb": ram_gb,
        "storage_gb": storage_gb,
        "is_macos": is_macos,
    }

    laptops.append(laptop)
    data_to_save = {"laptops": laptops}

    try:
        with open(PICKLE_PATH, "wb") as pickle_file:
            pickle.dump(data_to_save, pickle_file)

        print(
            f"\nLaptop {laptop['brand']} {laptop['model']} "
            f"with ID {laptop['id']} added successfully!"
        )
        print("Operation completed.\n")

    except Exception as exc:
        print(f"Error saving changes: {exc}")
