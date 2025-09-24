import json
#Add Laptop to the JSON file
def add_laptop():
	print("Enter new laptop details:")
	laptop = {}
	#Enter Laptop ID 
	laptop['id'] = input("ID: ")
	#Validate that Laptop ID is not empty
	if not laptop['id']:
		print("Error: ID must not be empty.")
		return
	laptop['brand'] = input("Brand: ")
	if not laptop['brand']:
		print("Error: Brand must not be empty.")
		return
	laptop['model'] = input("Model: ")
	if not laptop['model']:
		print("Error: Model must not be empty.")
		return
	laptop['processor'] = input("Processor: ")
	if not laptop['processor']:
		print("Error: Processor must not be empty.")
		return
	try:
		laptop['ram_gb'] = int(input("RAM (GB): "))
	except ValueError:
		laptop['ram_gb'] = 0
	try:
		storage_capacity = int(input("Storage Size (GB): "))
	except ValueError:
		storage_capacity = 0
	laptop['storage-size_gb'] = storage_capacity
	# Betriebssystem: 0 = Windows, 1 = MacOS
	os_input = input("Is this a MacOS device? (y/n): ").strip().lower()
	laptop['is_macos'] = os_input == 'y'

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
