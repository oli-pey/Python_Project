# Laptop Inventory Manager
## Problem
 Many small businesses or individuals who manage multiple laptops don’t have a simple tool to track their device inventory with details like RAM, storage, model, etc. They often use spreadsheets, text files, or manual notetaking, which can lead to errors, missing records, and difficulty filtering or deleting entries.    Our program addresses this by providing a console tool to __store, display,add, filter, and delete__ laptop entries in a structured, persistent Form.
## Scenarios
A user (e.g. a small-scale IT manager or tech hobbyist) launches the main.py file in a terminal. They see a menu of options (Display Inventory, Create Laptop, Delete Laptop, Filter Laptop and exit the programm).
- If the user chooses __Display Inventory__, a list will appear in the console displaying all the laptops with their criteras such as Brand,Model and other attributes.
- If the user chooses __Create Laptop__, the user will be gudied through a list of inputs to add the details and configuration of the new Laptop. During the input of the data the programm will check for its validity esuring no wring inputs for examplse not two laptops with the same ID or no strange ram numbers like 37 GBs
- If the user chooses __Delete Laptop__, a list of all the current inventory will appear and the user is promted to enter a laptop ID. The entered laptop id is then checked in the list for a valid laptop and if exists it will be deleted from the inventory.
- If the user chooses __Filter Laptop__, he will be guided to a another menu where he can choose by what criteria he wishes to filter the inventory by. After that choice he will be prompted to enter one value or even two values to filter the inventory by. For example filter by brand and then the user inputs Apple, then all laptops with the brand Apple will appear.
  The project uses the Python built-in pickle module to handle all data persistence (writing, reading, and deletion) to a binary file named [inventory.pkl.]
## User Stories
- As a user, I want to see all stored laptops displayed in a formatted table with all key criteria (ID, Brand, Model, Processor, RAM, Storage, and OS), because it allows me to quickly and clearly review my entire current inventory.
- As a user, I want to be guided through a series of distinct inputs to create a new laptop entry, because it ensures all necessary details and configurations are recorded correctly.
- As a user, I want robust input validation during the creation process (e.g., checking for unique 4-digit IDs, ensuring RAM/Storage are multiples of 8GB/256GB, and validating against allowed brands/processors), because it prevents data entry errors and maintains high data quality.
- As a user, I want to delete a specific laptop entry by entering its unique ID after viewing the current inventory, because it helps me accurately keep the inventory up to date when a device is sold or removed.
- As a user, I want to filter the inventory by single criteria (Brand, Min RAM, or Min Storage) or a combination (Min RAM AND Min Storage), because it saves time when searching for specific device configurations that meet hardware or manufacturer requirements.
- As a user, I want all changes (additions and deletions) to be immediately saved to the data file, so that when I next run the app, I don’t lose any data and the inventory remains consistent.
- As a user, I want to be able to type 'back' or 'exit' at any input prompt to cancel the current operation (Create, Delete, Filter) and return to the main menu, because it allows me to quickly navigate the application and prevent accidental data entry or modification.
## Use Cases
| Use Case | Goal / Description | Key Functions Involved |
| :--- | :--- | :--- |
| **Display Inventory** (Menu Option 1) | To load and display the complete list of laptops from the persistent data file (`inventory.pkl`) in a formatted table. | `main()`, `display_inventory()`, `load_inventory()`, `print_laptop_list()` |
| **Create Laptop** (Menu Option 2) | To guide the user through a set of validated inputs to define a new laptop, append it to the inventory, and save the updated list to `inventory.pkl`. | `main()`, `create_laptop()`, input validation helpers, `pickle.dump()` |
| **Delete Laptop** (Menu Option 3) | To display the current inventory, prompt the user for a valid Laptop ID, remove the corresponding entry, and save the change back to the `inventory.pkl` file. | `main()`, `delete_laptop()`, `display_inventory()`, `pickle.dump()` |
| **Filter Inventory** (Menu Option 4) | To present a filter menu and display a subset of the inventory that matches the user's selected criteria (e.g., Min RAM, Brand, or a combination). | `main()`, `filter_laptops()`, `get_numeric_input()`, `get_brand_input()`, `print_results()` |
## Project Requirements
| Category | Requirement Description | Implementation Details / Citation |
| :--- | :--- | :--- |
| **1. Interactive App (Console Input)** | **Main Menu System** | The application must feature a menu requiring console input in `main.py`. |
| | **Function Execution** | Based on the user’s selection, the program must call the corresponding function (display, create, delete, filter). |
| | **Flexible navigation** | The program must allow users to exit a sub-menu (Create, Delete, Filter) and return to the main menu by typing a specific keyword (e.g., 'back' or 'exit') at any input prompt.|
| **2. Data Validation** | **Menu Choice Validation** | Check whether the user’s input is a digit and corresponds to a valid menu option. |
| | **Imputed Data Validation** | Validate imputed data when adding a new laptop (e.g., ensuring RAM input is a valid integer). |
| | **Pickle File Handling** | When loading the pickled file, handle errors such as "file not found" or "unpickling error" using a `try/except` block, and initialize an empty list if needed. |
| **3. File Processing** | **Loading Data (Input)** | At startup, the program must attempt to open a pickle file (`inventory.pkl`) to load the existing list of laptop objects. |
| | **Saving Data (Output)** | After operations that modify the inventory (delete, create), the program must write the updated list back to the pickle file. |
| | **Data Persistence** | The file processing ensures that when the program is restarted, all prior changes remain intact. |
