from opcode import opname


# Add a discount to an item
def add_discount():
    item = input("Enter the item to add a discount to: ")
    discount_rate = float(input(f"Enter the discount rate (in percentage) for {item}: "))
    
    with open("menu.txt", "r") as file:
        items = file.readlines()
    
    updated_items = []
    item_found = False
    
    for line in items:
        name, price = line.strip().split(",")[:2]
        price = float(price)
        if name == item:
            item_found = True
            discounted_price = price * (1 - discount_rate / 100)
            updated_items.append(f"{name},{discounted_price:.2f}\n")
        else:
            updated_items.append(line)
    
    if not item_found:
        print(f"Item '{item}' not found in the menu.")
        return
    
    with open("menu.txt", "w") as file:
        file.writelines(updated_items)
    
    print(f"Discount of {discount_rate}% has been applied to '{item}'.")
    print("\nUpdated Menu:")
    with open("menu.txt", "r") as file:
        print(file.read())








# Delete a discount from an item
def delete_discount():
    item = input("Enter the item to remove discount from: ")
    
    updated = False
    try:
        with open("menu.txt", "r") as file:
            items = file.readlines()

        with open("menu.txt", "w") as file:
            for line in items:
                name, price, *discount = line.strip().split(",")
                if name == item and discount:
                    file.write(f"{name},{price}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print(f"Discount removed from '{item}'.")
        else:
            print(f"Item '{item}' either not found or had no discount.")
    except FileNotFoundError:
        print("Menu file not found.")




        

# Modify an existing discount for an item
def modify_discount():
    item = input("Enter the item to modify the discount for: ")
    new_discount_rate = float(input("Enter the new discount rate (in decimal): "))
    
    updated = False
    try:
        with open("menu.txt", "r") as file:
            items = file.readlines()

        with open("menu.txt", "w") as file:
            for line in items:
                name, price, *discount = line.strip().split(",")
                if name == item and discount:
                    file.write(f"{name},{price},{new_discount_rate}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print(f"Discount for '{item}' updated to {new_discount_rate * 100}%.")
        else:
            print(f"Item '{item}' either not found or has no existing discount.")
    except FileNotFoundError:
        print("Menu file not found.")





# Billing
def load_users(file_path):
    users = set()
    with open(file_path, 'r') as file:
        for line in file:
            role, username, password = line.strip().split(',')
            users.add(username)
    return users

def generate_bill():
    username = input("Enter your username: ")
    cart_file = input("Enter your cart file name: ")
    users_file = input("Enter your users file name: ")
    bill_file = input("Enter the bill file name: ")

    users = load_users(users_file)
    
    if username not in users:
        print("Username not found in users.txt.")
        return
    
    try:
        with open(cart_file, 'r') as cart, open(bill_file, 'w') as bill:
            bill.write(f"{username},\n")
            for line in cart:
                food_item, quantity, price = line.strip().split(',')
                bill.write(f"Content: {food_item}, Quantity: {quantity}, Final_price: {price}\n")
        
        print(f"Bill has been generated in {bill_file}.")
    
    except FileNotFoundError:
        print("One or more files could not be found. Please check the file paths.")


