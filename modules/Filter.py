import pickle

def filter_laptops():
    print("\n==============================")
    print("   FILTER LAPTOP INVENTORY")
    print("==============================\n")
    

    filterchoice = input("What category would you like to filter the Laptops by?\n"
                          "1. RAM Size\n"
                          "2. Storage Size\n"
                          "3. Operating System (MacOS/Windows)\n"
                          "Your choice: ")
    

    if filterchoice == "1":
        ramfilter = int(input("Enter the minimum RAM size (GB) to filter by: "))
        filter_key = 'ram_gb'
        filter_value = ramfilter


    
    else:
        print("Invalid choice")
        exit()

# Filter laptops based on user input


    if __name__ == '__main__':
        filter_laptops()
     
    
