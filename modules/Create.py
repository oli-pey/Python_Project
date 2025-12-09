import pickle
import os

# -------------------------------
#   CONSTANTS
# -------------------------------
ALLOWED_BRANDS = ["Dell", "HP", "Lenovo", "Asus", "Acer", "Apple"]

ALLOWED_PROCESSORS = [
    "Intel Core i3", "Intel Core i5", "Intel Core i7", "Intel Core i9",
    "AMD Ryzen 3", "AMD Ryzen 5", "AMD Ryzen 7", "AMD Ryzen 9",
    "Apple M1", "Apple M2", "Apple M3"
]

def create_laptop():
    """
    Handles interactive creation of a laptop entry and stores it in inventory.pkl.
    """

    print("\n==============================")
    print("   ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")

    pickle_path = "data/inventory.pkl"

    # -------------------------------
    #   LOAD EXISTING INVENTORY (ROBUST)
    # -------------------------------
    # 1. Initialize data with a default value so it always exists
    data = {"laptops": []}

    # 2. Try to load the file
    if os.path.exists(pickle_path):
        try:
            with open(pickle_path, 'rb') as f:
                data = pickle.load(f)
                    # Ensure 'laptops' key exists, even if the dict is empty
                if "laptops" not in data:
                    data["laptops"] = []
                else:
                    # If the file contains something else (like a list), reset it
                    print("Warning: File format incorrect. Starting with empty inventory.")
                    data = {"laptops": []}

        except Exception:
            # Handle corrupted files, empty files, or permission errors
            print("Warning: Could not read inventory file. Starting with empty inventory.")
            data = {"laptops": []}

    # Extract existing laptop IDs (used for uniqueness validation)
    existing_ids = [laptop.get("id") for laptop in data["laptops"]]

    # -------------------------------
    #   INPUT VALIDATION FUNCTIONS
    # -------------------------------

    def laptop_id_input():
        while True:
            laptop_id = input("Enter laptop ID (4 digits): ").strip()

            if not laptop_id:
                print("Laptop ID cannot be empty.")
                continue

            if not laptop_id.isdigit():
                print("Laptop ID must be numeric.")
                continue

            if len(laptop_id) != 4:
                print("Laptop ID must be exactly 4 digits.")
                continue

            laptop_id = int(laptop_id)
            if laptop_id in existing_ids:
                print(f"Laptop ID '{laptop_id}' already exists. Choose another.")
                continue

            return laptop_id

    def brand_input():
        while True:
            brand = input("Enter laptop manufacturer: ").strip()

            if not brand:
                print("Brand cannot be empty.")
                continue

            if brand not in ALLOWED_BRANDS:
                print(f"Invalid brand. Allowed brands: {', '.join(ALLOWED_BRANDS)}")
                continue

            return brand

    def model_input():
        while True:
            model = input("Enter laptop model: ").strip()

            if not model:
                print("Model cannot be empty.")
                continue

            if len(model) > 25:
                print("Model name too long (max 25 characters).")
                continue

            return model

    def processor_input():
        print(f"Allowed Processors: {', '.join(ALLOWED_PROCESSORS)}")
        while True:
            processor = input("Enter processor: ").strip()

            if processor in ALLOWED_PROCESSORS:
                return processor

            print("Invalid processor. Select from the list above.")

    def ram_input():
        while True:
            ram_value = input("Enter RAM in GB: ").strip()

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
        while True:
            try:
                storage_gb = int(input("Enter storage in GB: "))

                if not (256 <= storage_gb <= 2048):
                    print("Storage must be between 256GB and 2048GB.")
                    continue
                if storage_gb % 256 != 0:
                    print("Storage must be a multiple of 256GB.")
                else:
                    return storage_gb

            except ValueError:
                print("Please enter a numeric value.")

    def os_input():
        while True:
            os_name = input("Enter OS (Windows/macOS): ").strip().lower()

            if os_name == "macos":
                return True
            if os_name == "windows":
                return False

            print("Invalid input. Enter 'Windows' or 'macOS'.")

    # -------------------------------
    #   CAPTURE LAPTOP DETAILS
    # -------------------------------
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
    data["laptops"].append(laptop)

    # We use a try/except here too, just in case of permission errors while saving
    try:
        with open(pickle_path, "wb") as f:
            pickle.dump(data, f)
        
        print(f"\nLaptop '{laptop['brand']} {laptop['model']}' "
              f"with ID '{laptop['id']}' added successfully!")
        print("Operation completed.\n")
        
    except Exception as e:
        print(f"Error: Could not save to file. {e}")

# Run the function
if __name__ == "__main__":
    create_laptop()