import os
import pickle
from config.config import PICKLE_PATH


def display_inventory():
    """Load and display the current inventory of laptops."""
    laptops = load_inventory()

    if laptops is None:
        print("Error loading inventory.")
        return

    if not laptops:
        print("The inventory is currently empty.")
        return

    print_laptop_list(laptops)


def load_inventory():
    """
    Load laptop data from the pickle file defined in PICKLE_PATH.

    Returns:
        list or None: A list of laptops, or None if an error occurs.
    """
    if not os.path.exists(PICKLE_PATH):
        return []

    try:
        with open(PICKLE_PATH, "rb") as pickle_file:
            data = pickle.load(pickle_file)

        return data.get("laptops", [])

    except Exception as exc:
        print(
            "Critical Error: Could not read or unpickle inventory file: "
            f"{exc}"
        )
        return None


def print_laptop_list(laptops):
    """Print the details of the given list of laptops in a formatted table."""
    header = (
        f"{'ID':<6} {'Brand':<12} {'Model':<25} "
        f"{'Processor':<25} {'RAM':<10} {'Storage':<12} {'OS':<8}"
    )
    print(header)
    print("-" * 110)

    for laptop in laptops:
        laptop_id = laptop.get("id", "")
        brand = laptop.get("brand", "")
        model = laptop.get("model", "")
        processor = laptop.get("processor", "")

        ram_gb = laptop.get("ram_gb")
        storage_gb = laptop.get("storage_gb")

        ram = f"{ram_gb} GB" if ram_gb is not None else ""
        storage = f"{storage_gb} GB" if storage_gb is not None else ""

        os_name = "macOS" if laptop.get("is_macos", False) else "Windows"

        print(
            f"{str(laptop_id):<6} {brand:<12} {model:<25} "
            f"{processor:<25} {ram:<10} {storage:<12} {os_name:<8}"
        )
