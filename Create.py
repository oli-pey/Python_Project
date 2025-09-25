import pickle
import os

def create_laptop(laptop, pickle_path='inventory.pkl'):
    
	# Lade bestehende Daten oder erstelle neue Struktur
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as f:
            data = pickle.load(f)
    else:
        data = {"laptops": []}
    # Füge das neue Laptop hinzu
    data["laptops"].append(laptop)
    with open(pickle_path, 'wb') as f:
        pickle.dump(data, f)
    print("Laptop added successfully.")

if __name__ == '__main__':
    new_laptop = {
        "id": "LAP021",
        "brand": "TestBrand",
        "model": "TestModel",
        "processor": "TestProcessor",
        "is_macos": False,
        "ram_gb": 8,
        "storage-size_gb": 256
    }
    create_laptop(new_laptop)