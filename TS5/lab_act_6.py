class exeption_handeling:
    def __init__(self, choice):
     self.choice = choice
    def main_choice(self):
     try:
         print("")
         self.choice = int(input("Enter your choice: "))
         return self.choice
     except ValueError:
         print("")
         print("Input must be a number between 1 and 4!")
         return 0
    def choice_check(self):
     if self.choice >= 6 or self.choice <= 0:
         print("")
         print("Invalid choice!") 
         return 0
     else:
         return choice

class define_items:
    def __init__(self, id, name, description, price):
     self.id = id
     self.name = name
     self.description = description
     self.price = price
     
    def input_id(self):
     try:
         print("")
         self.id = int(input("Enter ID (3 digits): "))
         if self.id < 100 or self.id > 999:
            print("")
            print("Input must be a 3-digit number!")
            return 0
         else:
            return self.id
     except ValueError:
         print("")
         print("Input must be a number!")
         return 0 
    
    def input_price(self):
        if self.price > 100000 or self.price < 0:
            print("")
            print("Price must be between 0 and 100000 dollers!")
            return 0
        else:
            return self.price
         
def main_menu():
    
    print("\n[1] Create")
    print("[2] Read")
    print("[3] Update")
    print("[4] Delete")
    print("[5] Exit")

def update_menu():
    
    print("\n[1] Update ID")
    print("[2] Update Name")
    print("[3] Update Description")
    print("[4] Update Price")
    print("[5] Exit")
    
check = 0

choice = 0

id = 0

name = ""

description = ""

price = 0.00

items = define_items(id, name, description, price)

def enter_id(temp_id):
    check_id = 0
    while check_id == 0:
        id = define_items.input_id(items)
        temp_id = id
        check_id = id
    return temp_id

def enter_name(temp_name):
    print("")
    name = input("Enter Item Name: ")
    temp_name = name
    return temp_name

def enter_description(temp_description):
    print("")
    desc = input("Enter Item Description: ")
    temp_description = desc
    return temp_description

def enter_price(temp_price):
    check_price = 0 
    while check_price == 0:
        print("")
        price = float(input("Enter Price: "))
        items.price = price
        new_price = define_items.input_price(items)
        temp_price = price
        check_price = new_price
    return temp_price
               
def open_file():
    file = open("items.txt", "a+")
    file.write("ID               || {0}\nITEM NAME        || {1}\nITEM DESCRIPTION || {2}\nITEM PRICE       || {3}\n".format(0, "DO NOT DELTE THIS", "DO NOT DELTE THIS", 0))
    file.close()
def save_file(id, name, description, price):
    file = open("items.txt", "a+")
    file.write("\nID               || {0}\nITEM NAME        || {1}\nITEM DESCRIPTION || {2}\nITEM PRICE       || {3}\n".format(id, name, description, price))
    file.close()
    print("")
    print("Items has been saved")
def check_file():
    try:
        check_file = open("items.txt", "r")
        check_file.close() 
    except FileNotFoundError:
        open_file()
def read_file():
    file = open("items.txt", "r")
    print(file.read())
    file.close()
    
def update_menu():
    
    print("\n[1] Update ID")
    print("[2] Update Name")
    print("[3] Update Description")
    print("[4] Update Price")
    print("[5] Exit")

def update_file():
    
    read_file()
    
    with open("items.txt", "r") as file:
        lines = file.readlines()
        found_id = False
        print("")
        line_number = int(input("Enter ID to update: "))
        for i in range(0, len(lines), 5):  
            new_id = (lines[i].replace("ID               || ", "").strip())
            new_name = (lines[i + 1].replace("ITEM NAME        || ", "").strip())
            new_description = (lines[i + 2].replace("ITEM DESCRIPTION || ", "").strip())
            new_price = (lines[i + 3].replace("ITEM PRICE       || ", "").strip())
            if line_number == int(new_id):
                found_id = True
                update_menu()
                up_choice = int(input("Enter your choice: "))
                print("")
                if up_choice == 1:
                    new_id = enter_id(new_id)
                    lines[i] = "ID               || " + str(new_id) + "\n"
                elif up_choice == 2:
                    new_name = input("Enter new Name: ")
                    lines[i + 1] = "ITEM NAME        || " + new_name + "\n"
                elif up_choice == 3:
                    new_description = input("Enter new Description: ")
                    lines[i + 2] = "ITEM DESCRIPTION || " + new_description + "\n"
                elif up_choice == 4:
                    new_price = enter_price(new_price)
                    lines[i + 3] = "ITEM PRICE       || " + str(new_price) + "\n"
                elif up_choice == 5:
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice")
                    return update_file()
        if found_id:
            with open("items.txt", "w") as file:
                file.writelines(lines)
            print("")
            print("Item updated")
        else:
            print("ID not found")
            update_file()

def delete_item():
    
    read_file()
    
    with open("items.txt", "r") as file:
        lines = file.readlines()
        print("")
        line_number = int(input("Enter ID to delete: "))
        print("")
        found_id = False
        
        for i in range(0, len(lines), 5):  
            new_id = (lines[i].replace("ID               || ", "").strip())
            if line_number == int(new_id):
                found_id = True
                print(f"ID: {new_id}")
                print(f"Name: {lines[i + 1].replace('ITEM NAME        || ', '').strip()}")
                print(f"Description: {lines[i + 2].replace('ITEM DESCRIPTION || ', '').strip()}")
                print(f"Price: {lines[i + 3].replace('ITEM PRICE       || ', '').strip()}")
                print("")
                confirm = input("Are you sure you want to delete this item? (yes/no): ").strip().lower()
                if confirm == 'yes':
                    del lines[i:i+5]
                elif confirm == 'no':
                    print("")
                    print("Deletion cancelled.")
                else:
                    print("")
                    print("Invalid choice.")
                    print("")
                    delete_item()
                break
        if found_id and confirm == 'yes':
            with open("items.txt", "w") as file:
                file.writelines(lines)
            print("")
            print("Item deleted")
        elif not found_id:
            print("ID not found")
            delete_item()

check_file()
while check != 5:
    
    error_check = 0
    choice = 0
    error = exeption_handeling(choice)
    
    while error_check == 0:
        
        main_menu()
        
        choice = error.main_choice()
        error_check = error.choice_check()
        
    if choice == 1:
        
        id = enter_id(id)
        name = enter_name(name)
        description = enter_description(description) 
        price = enter_price(price)
        
        item = define_items(id, name, description, price)
        save_file(item.id, item.name, item.description, item.price)
        
    elif choice == 2:
        
        print("\nRead\n")
        read_file()
        
    elif choice == 3:
        
        update_file()
        
    elif choice == 4:
        
        delete_item()
        
    elif choice == 5:
        print("\nExiting...\n")
        check = 5

