import os
import pickle

PICKLE_PATH = 'data/test.pkl'


def load_inventory():
    laptops = []

    if os.path.exists(PICKLE_PATH):
        try:
            with open(PICKLE_PATH, 'rb') as f:
                data = pickle.load(f)
                laptops = data.get('laptops', [])
        except Exception:
            print("Error: Could not read inventory file.")
            laptops = []

    return laptops


def _print_results(laptops):
    if not laptops:
        print('No laptops match the filter criteria.')
        return

    print(f"Found {len(laptops)} matching laptop(s):")
    print(f"{'ID':<6} {'Brand':<12} {'Model':<25} {'RAM':<8} {'Storage':<10} {'OS':<8}")
    print('-' * 70)
    for l in laptops:
        lid = l.get('id', '')
        brand = l.get('brand', '')
        model = l.get('model', '')
        ram = f"{l.get('ram_gb', '')} GB" if l.get('ram_gb') is not None else ''
        storage = f"{l.get('storage_gb', '')} GB" if l.get('storage_gb') is not None else ''
        os_name = 'MacOS' if l.get('is_macos', False) else 'Windows'
        print(f"{str(lid):<6} {brand:<12} {model:<25} {ram:<8} {storage:<10} {os_name:<8}")


def filter_laptops():
    print('\n==============================')
    print('   FILTER LAPTOP INVENTORY')
    print('==============================\n')

    laptops = load_inventory()
    if not laptops:
        print('No laptops found in inventory.')
        return

    while True:
        print('\nFilter by:')
        print(' 1) Minimum RAM (GB)')
        print(' 2) Minimum Storage (GB)')
        print(' 3) Operating System (macos/windows)')
        print(" q) Quit")
        choice = input('Your choice: ').strip().lower()

        if choice in ('q', 'quit', 'exit'):
            return

        if choice == '1':
            try:
                min_ram = int(input('Min RAM (GB): ').strip())
                results = [l for l in laptops if int(l.get('ram_gb', 0)) >= min_ram]
            except ValueError:
                print('Please enter a numeric RAM value.')
                continue

        elif choice == '2':
            try:
                min_storage = int(input('Min Storage (GB): ').strip())
                results = [l for l in laptops if int(l.get('storage_gb', 0)) >= min_storage]
            except ValueError:
                print('Please enter a numeric storage value.')
                continue

        elif choice == '3':
            os_choice = input('OS (macos/windows): ').strip().lower()
            if os_choice not in ('macos', 'windows'):
                print("Enter 'macos' or 'windows'.")
                continue
            want_macos = (os_choice == 'macos')
            results = [l for l in laptops if bool(l.get('is_macos', False)) == want_macos]

        else:
            print('Invalid choice.')
            continue

        _print_results(results)

        if input('\nRun another filter? (y/n): ').strip().lower() not in ('y', 'yes'):
            break


if __name__ == '__main__':
    filter_laptops()

