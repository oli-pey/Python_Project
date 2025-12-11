import pickle
from modules.Display import load_inventory
from config.config import PICKLE_PATH, ALLOWED_BRANDS,ALLOWED_PROCESSORS

def create_laptop():
    print("\n==============================")
    print("   ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")

    laptops = load_inventory()
    existing_ids = [laptop.get("id") for laptop in laptops]

    # -------------------------------
    #   INPUT VALIDATION FUNCTIONS
    # -------------------------------
    def laptop_id_input():
        while True:
            laptop_id_str = input("Enter laptop ID (4 digits): ").strip()           
            if not laptop_id_str:
                print("Laptop ID cannot be empty.")
            elif not laptop_id_str.isdigit():
                print("Laptop ID must be numeric.")
            elif len(laptop_id_str) != 4:
                print("Laptop ID must be exactly 4 digits.")
            else:
                laptop_id = int(laptop_id_str)
            if laptop_id in existing_ids:
                print(f"Laptop ID {laptop_id} already exists. Choose another.")
            else:
                return laptop_id 
            
    def brand_input():
        while True:
            brand = input("Enter laptop manufacturer: ").strip()
            if not brand:
                print("Brand cannot be empty.")
            elif brand not in ALLOWED_BRANDS:
                print(f"Invalid brand. Allowed brands: {", ".join(ALLOWED_BRANDS)}")
            else:
                return brand

    def model_input():
        while True:
            model = input("Enter laptop model: ").strip()
            if not model:
                print("Model cannot be empty.")
            elif len(model) > 25:
                print("Model name too long (max 25 characters).")
            else:
                return model

    def processor_input():
        print(f"Allowed Processors: {", ".join(ALLOWED_PROCESSORS)}")
        while True:
            processor = input("Enter processor: ").strip()
            if not processor in ALLOWED_PROCESSORS:
                print("Invalid processor. Please choose from the allowed list.")
            else:
                return processor

    def ram_input():
        while True:
            ram_value = input("Enter RAM in GB: ").strip()
            if not ram_value.isdigit():
                print("Please enter a numeric value.")
                continue
            ram_gb = int(ram_value)
            if not (8 <= ram_gb <= 256):
                print("RAM must be between 8GB and 256GB.")
            elif ram_gb % 8 != 0:
                print("RAM must be a multiple of 8GB.")
            else:
                return ram_gb

    def storage_input():
        while True:
            storage_value = input("Enter storage in GB: ").strip()
            if not storage_value.isdigit():
                print("Please enter a numeric value.")
                continue
            storage_gb = int(storage_value)
            if not (256 <= storage_gb <= 2048):
                print("Storage must be between 256GB and 2048GB.")
            elif storage_gb % 256 != 0:
                print("Storage must be a multiple of 256GB.")
            else:
                return storage_gb

    def os_input():
        while True:
            os_name = input("Enter OS (Windows/macOS): ").strip().lower()
            if os_name == "macos":
                return True
            if os_name == "windows":
                return False
            print("Invalid input. Enter Windows or macOS.")

    #   CAPTURE LAPTOP DETAILS
    laptop = {
        "id": laptop_id_input(),
        "brand": brand_input(),
        "model": model_input(),
        "processor": processor_input(),
        "ram_gb": ram_input(),
        "storage_gb": storage_input(),
        "is_macos": os_input(),
    }

    # -------------------------------
    #   SAVE TO INVENTORY
    # -------------------------------
    
    # Append the new laptop to the list we loaded earlier
    laptops.append(laptop)
    
    # Re-wrap it in a dictionary structure for saving
    data_to_save = {"laptops": laptops}

    try:
        with open(PICKLE_PATH, "wb") as f:
            pickle.dump(data_to_save, f)
        
        # Fixed syntax: used single quotes inside f-string keys
        print(f"\nLaptop {laptop['brand']} {laptop['model']} "
              f"with ID {laptop['id']} added successfully!")
        print("Operation completed.\n")
        
    except Exception:
        print("Error: Could not save to file.")