# Laptop Inventory Manager
## Problem
 Many small businesses or individuals who manage multiple laptops don’t have a simple tool to track their device inventory with details like RAM, storage, model, etc. They often use spreadsheets, text files, or manual notetaking, which can lead to errors, missing records, and difficulty filtering or deleting entries.    Your program addresses this by providing a console tool to __store, display, filter, and delete__ laptop entries in a structured, persistent Form.
## Scenario
A user (e.g. a small-scale IT manager or tech hobbyist) launches your main.py in a terminal. They see a menu of options (Show Inventory, Display Laptop, Delete Laptop, Filter Laptop, etc.).
- If they choose __Show Inventory__, the program lists all laptops currently stored.
- If they choose __Display Laptop__, they can input an identifier (e.g. index or ID) to view one laptop’s detailed specs.
- If they choose __Delete Laptop__, they input which laptop to remove.
- If they choose __Filter Laptop__, they input criteria (e.g. “RAM > 16”) and the program shows matching laptops.
  All operations read from and write to a __pickle file__ that stores the list of laptop objects, so the inventory is persistent across runs.
## User Stories
- As a user, I want to __see all stored laptops__. 
- As a user, I want to __delete__ a laptop entry.
- As a user, I want to __filter laptops__ by criteria (e.g. RAM, storage) to find ones meeting requirements.
- As a user, I want all changes to persist (so when I next run the app, I don’t lose data).
- As a user, I want input validation so I don’t crash the program by entering invalid values.
## Use Cases
- Display Inventory (from inventory.pkl)
- Delete Laptop (from inventory.pkl)
- Create Laptop (with imput validation and write to inventory.pkl)
- Filter Inventory ( Display Items from inventory.pkl matching filter criteria)
## Project Requirements
### 1. Interactive App (Console Input)
- Menu requiring console input in main.py
- Based on the user’s selection, the program calls the corresponding function (show, display, delete, filter).
### 2. Data Validation
- Menu choice: check whether the user’s input is a digit and corresponds to a valid menu option (e.g. if not choice.isdigit() or int(choice) not in allowed options: …).
- Validation of imputed data when adding a new laptop (example ram only allow int)
- When loading the pickled file: handle errors such as “file not found” or “unpickling error” with try/except and initialize an empty list if needed.
### 3. File Processing
Your program reads and writes data from disk using the Python pickle module (or similar).
- __Input / Loading__: At startup, the program attempts to open a pickle file (e.g. laptops.pkl) to load the existing list of laptop objects. If the file doesn’t exist or is corrupted, it initializes an empty list.
- __Output / Saving__: After operations that mutate the inventory (delete, possibly additions if you add that later), the program writes the updated list back to the pickle file.
- The persistence ensures that when the program is restarted, all prior changes remain intact.
