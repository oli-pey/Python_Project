import pickle
def delete_Laptop(laptop_id):
    with open('inventory.pkl', 'rb') as f:
        data = pickle.load(f)
    laptops = data.get('laptops', [])
    
    # Remove laptops with the matching id
    laptops = [laptop for laptop in laptops if laptop.get('id') != laptop_id]
    data['laptops'] = laptops
    with open('inventory.pkl', 'wb') as f:
        pickle.dump(data, f)
    print(f"Laptop with ID '{laptop_id}' has been removed (if it existed).")

if __name__ == '__main__':
    print("\n==============================")
    print("   REMOVE LAPTOP FROM INVENTORY")
    print("==============================\n")
    laptop_id = input("Please enter the Laptop ID to remove: ")
    print("\nProcessing removal...\n")
    delete_Laptop(laptop_id)
    print("\nOperation completed.\n")
