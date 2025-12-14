# 📈 Project Status Report: Laptop Inventory Manager

**Reporting Date:** December 10, 2025 (Final Progress Report)
**Project Title:** Laptop Inventory Manager (Console Application)
**Timeline:** October 13, 2025 – December 10, 2025 (Reporting Period: Bi-weekly / Tri-weekly on Wednesdays)

---

## 🎯 Project Goals

The primary goal is to create a reliable, console-based tool to replace manual tracking methods (like spreadsheets) for managing a laptop inventory.

The application must support the following core functionalities:

* **Store & Persist:** Maintain a structured inventory list and save all changes persistently to `inventory.pkl` using the `pickle` module.
* **Display:** Show all stored laptops in a formatted, clear table.
* **Create (Add):** Guide the user through input to add new laptops with strict validation checks (e.g., unique ID, RAM/Storage multiples).
* **Delete:** Remove a specific laptop entry by its unique ID.
* **Filter:** Allow users to search the inventory by single or combined criteria (Brand, Min RAM, Min Storage).
* **Navigate:** Provide flexible navigation, allowing the user to type 'back' or 'exit' to return to the main menu from any sub-operation.

---

## ✅ Management Success Criteria Assessment

| Criteria | Status | Evidence from Implementation |
| :--- | :--- | :--- |
| Project Goals Clearly Defined | **COMPLETE** | Goals were set in the `readme.md` and implemented via dedicated Python functions in `main.py`. |
| Tasks Identified | **COMPLETE** | Key functions were identified in the Use Cases and mapped directly to modules (`create.py`, `delete.py`, `filter.py`, `display.py`). |
| Commitment Kept | **COMPLETE** | Commitment to quality is demonstrated by implementing robust validation rules (e.g., RAM/Storage multiples) and error handling for data persistence. |
| Steady Progress Shown | **COMPLETE** | Progress was managed successfully over a bi-weekly to tri-weekly schedule, including successful resolution of a key technical challenge (see Project Challenge below). |

---

## ⚠️ Project Challenge: Implementing Flexible Navigation (T11)

A notable challenge arose during the implementation of the "Flexible navigation" requirement (T11), which mandated the user must be able to type 'back' or 'exit' at any input prompt to cancel the operation and return to the main menu.

A notable challenge arose during the implementation of the "flexible navigation" requirement (T11), which required that users be able to type 'back' or 'exit' at any input prompt to cancel the operation and return to the main menu.

* The **Problem:** was that the `create_laptop()` function was heavily structured with sequential calls to multiple nested validation helper functions (e.g., `laptop_id_input()`, `brand_input()`, `model_input()`, etc.). Implementing 'back' required each of these seven nested functions to return a consistent signal (`None`) upon cancellation. It also required refactoring the main `create_laptop()` function to check for this signal after every input, preventing the next input function from executing prematurely.
* **Resolution:** A dedicated refactoring effort was required to enforce this flow. All helper functions were standardized to return `None` upon 'back' or 'exit', and the `create_laptop()` function was updated to include `"if result is None: return"` after every helper call. This ensures a clean and immediate return to the main menu when the user cancels.

---

## 📋 Identified Tasks and Completion Status

| Task ID | Description | Phase | Status |
| :--- | :--- | :--- | :--- |
| T1 | Define Laptop Data Structure (Class or Dict). | Setup/Data | **Completed** |
| T2 | Implement `load_inventory()` with file not found/unpickling error handling. | Setup/Data | **Completed** |
| T3 | Implement `save_inventory()` to persist data to `inventory.pkl`. | Setup/Data | **Completed** |
| T4 | Implement input validation helpers (e.g., unique ID, allowed Brand/Processor). | Creation/Deletion | **Completed** |
| T5 | Implement RAM/Storage validation helpers (multiples of 8GB/256GB). | Creation/Deletion | **Completed** |
| T6 | Implement `create_laptop()` guided input using validation helpers. | Creation/Deletion | **Completed** |
| T7 | Implement `delete_laptop()` with ID prompt and persistence update. | Creation/Deletion | **Completed** |
| T8 | Implement `print_laptop_list()` for formatted, readable table output. | Display/Filter | **Completed** |
| T9 | Implement `display_inventory()` (loads and prints T8). | Display/Filter | **Completed** |
| T10 | Implement Filter Menu and `filter_laptops()` logic (single and combo criteria). | Display/Filter | **Completed** |
| T11 | Implement flexible navigation ('back'/'exit') across all inputs. | Display/Filter | **Completed** |
| T12 | Final integration of all functions into `main()` menu loop and comprehensive testing. | Finalization | **Completed** |

---

## 📅 Progress Report Log

| Date (Wednesday) | Tasks Completed | Key Progress Achieved (Verification) |
| :--- | :--- | :--- |
| **Oct 15, 2025** | T1, T2, T3 | **Setup & Persistence Layer Established.** Defined the core data structure (T1). Successfully implemented the persistence layer using `pickle`, including robust error handling (`load_inventory` T2) and saving changes (`save_inventory` T3). |
| **Nov 5, 2025** | T4, T5, T6, T7 | **Core Modification Logic Complete (3-Week Period).** Implemented all input validation logic (T4, T5), enforcing rules like unique 4-digit ID and multiples of 8GB/256GB. Both the `create_laptop()` (T6) and `delete_laptop()` (T7) functions are fully functional and tested. |
| **Nov 26, 2025** | T8, T9, T10 | **Display and Filtering Functions Complete (3-Week Period).** Implemented the formatted table output via `print_laptop_list()` (T8). Completed the `display_inventory()` (T9) and the comprehensive `filter_laptops()` function (T10), which supports all required single and combined criteria searches. |
| **Dec 10, 2025** | T11, T12 | **Final Integration and Quality Assurance (2-Week Period).** Successfully implemented the challenging flexible navigation requirement (T11), requiring refactoring to ensure safe exit across all nested inputs. Completed final integration into `main.py` (T12) and passed all comprehensive testing. **Project Complete.** |

---
