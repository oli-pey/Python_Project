import pickle
import pprint

def print_pickle_inventory(pickle_path='inventory.pkl'):
    with open(pickle_path, 'rb') as f:
        data = pickle.load(f)
    pprint.pprint(data)

if __name__ == '__main__':
    print_pickle_inventory()
