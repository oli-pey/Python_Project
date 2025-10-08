import pickle
import Display

def delete_Laptop():
    # First show the current inventory so user can see what to delete
    print("\n==============================")
    print("   CURRENT LAPTOP INVENTORY")
    print("==============================\n")
    Display.display_inventory()
    
    print("\n==============================")
    print("   REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")
    laptop_id = input("Please enter the Laptop ID to remove: ")
    print("\nProcessing removal...\n")
    
    with open('inventory.pkl', 'rb') as f:
        data = pickle.load(f)
    laptops = data.get('laptops', [])
    
    # Check if laptop exists before deletion
    laptop_exists = any(laptop.get('id') == laptop_id for laptop in laptops)
    
    if not laptop_exists:
        print(f"No laptop found with ID '{laptop_id}'.")
        return
    
    # Remove laptops with the matching id
    laptops = [laptop for laptop in laptops if laptop.get('id') != laptop_id]
    data['laptops'] = laptops
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(data, f)
    print(f"Laptop with ID '{laptop_id}' has been successfully removed.")
    print("\nOperation completed.\n")

if __name__ == '__main__':
    delete_Laptop()
