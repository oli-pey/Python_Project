import json

def add_laptop():
	print("Enter new laptop details:")
	laptop = {}
	laptop['id'] = input("ID: ")
	laptop['brand'] = input("Brand: ")
	laptop['model'] = input("Model: ")
	laptop['processor'] = input("Processor: ")
	try:
		laptop['ram_gb'] = int(input("RAM (GB): "))
	except ValueError:
		laptop['ram_gb'] = 0
	storage_type = input("Storage Type (e.g., SSD/HDD): ")
	try:
		storage_capacity = int(input("Storage Capacity (GB): "))
	except ValueError:
		storage_capacity = 0
	laptop['storage'] = {
		'type': storage_type,
		'capacity_gb': storage_capacity
	}

	# Load existing data
	try:
		with open('inventory.json', 'r', encoding='utf-8') as f:
			data = json.load(f)
	except (FileNotFoundError, json.JSONDecodeError):
		data = {'laptops': []}

	data['laptops'].append(laptop)

	with open('inventory.json', 'w', encoding='utf-8') as f:
		json.dump(data, f, indent=2)
	print("Laptop added successfully!")

if __name__ == '__main__':
	add_laptop()
