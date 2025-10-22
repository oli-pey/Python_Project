# Laptop Inventory Manager

## Group Members
Benno Busche, Fabian Eppenberger, Georg von dem Bussche, Oliver Peyron
## Problem
 Many small businesses or individuals who manage multiple laptops don’t have a simple tool to track their device inventory with details like RAM, storage, model, etc. They often use spreadsheets, text files, or manual notetaking, which can lead to errors, missing records, and difficulty filtering or deleting entries. Our program addresses this by providing a console tool to __store, display, create, filter, and delete__ laptop entries in a structured, persistent Form.
## Scenario
A user (e.g. a small-scale IT manager or tech hobbyist) launches the programm. They see a menu of options 
(Display Laptop,Create Laptop Delete Laptop, and Filter Laptop).
- If the user chooses __Display Laptop__, a list of all laptops in the inventory will be printed out in the console.
- If the user chooses __create Laptop__, users are able to add new laptops into the inventory
- If the user chooses __Delete Laptop__, users are able to delete existing laptops by Laptop_ID
- If the user chooses __Filter Laptop__, users input a criteria (e.g. “RAM > 16”) and the program shows matching laptops.
  All operations read from and write to a __pickle file__ that stores the list of laptop objects, so the inventory is persistent across runs.
## User Stories
- As a user, I want to __see all stored laptops__, because it allows me to quickly review my current inventory without searching through files or notes.
- As a user, I want to __create__ new laptop entries, users should be able to enter the attributes for a new laptop in the console after a laptop has been added to the inventory the inventory should be displayed for the user to see the result.
- As a user, I want to __delete__ a laptop entry, because it helps me keep the inventory up to date when devices are sold, disposed of, or no longer needed.
- As a user, I want to __filter laptops__ by criteria (e.g. RAM, storage) to find ones meeting requirements, because it saves time when searching for specific device configurations and avoids manual sorting.
- As a user, I want all changes to persist (so when I next run the app, I don’t lose data), because it prevents data loss and ensures the inventory remains consistent between sessions.
- As a user, I want input validation so I don’t crash the program by entering invalid values, because it makes the tool reliable and user-friendly even for non-technical users.
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
Our program reads and writes data from disk using the Python pickle module (or similar).
- __Input / Loading__: At startup, the program attempts to open a pickle file (e.g. laptops.pkl) to load the existing list of laptop objects. If the file doesn’t exist or is corrupted, it initializes an empty list.
- __Output / Saving__: After operations that mutate the inventory (delete, possibly additions if you add that later), the program writes the updated list back to the pickle file.
- The persistence ensures that when the program is restarted, all prior changes remain intact.
