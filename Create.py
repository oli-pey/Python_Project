import pickle
import os

import pickle
import os

def create_laptop():
    print("\n==============================")
    print("   ADD NEW LAPTOP TO INVENTORY")
    print("==============================\n")
    
    # Get laptop information from user
    laptop_id = input("Enter laptop ID: ")
    brand = input("Enter brand: ")
    model = input("Enter model: ")
    processor = input("Enter processor: ")
    ram_gb = int(input("Enter RAM size (GB): "))
    storage_gb = int(input("Enter storage size (GB): "))
    os_choice = input("Is this a MacOS laptop? (y/n): ").lower()
    is_macos = os_choice == 'y' or os_choice == 'yes'
    
    # Create laptop dictionary
    laptop = {
        "id": laptop_id,
        "brand": brand,
        "model": model,
        "processor": processor,
        "is_macos": is_macos,
        "ram_gb": ram_gb,
        "storage-size_gb": storage_gb
    }
    
    # Load existing data or create new structure
    pickle_path = 'inventory.pkl'
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            data = pickle.load(f)
    else:
        data = {"laptops": []}
    
    # Check if laptop ID already exists
    existing_ids = [laptop_item.get('id') for laptop_item in data["laptops"]]
    if laptop_id in existing_ids:
        print(f"\nError: A laptop with ID '{laptop_id}' already exists!")
        print("Please choose a different ID.\n")
        return
    
    # Add the new laptop
    data["laptops"].append(laptop)
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)
    print(f"\nLaptop '{brand} {model}' with ID '{laptop_id}' added successfully!")
    print("Operation completed.\n")

if __name__ == '__main__':
    create_laptop()