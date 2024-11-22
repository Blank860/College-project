# delete account
def delete_account():
    account_to_delete = input("Which account would you like to delete: ")
    with open("users.txt", "r") as file:
        lines = file.readlines()
    updated_lines = []
    for line in lines:
        role, name, passw = line.strip().split(",")
        if name != account_to_delete:
            updated_lines.append(line)
    if len(updated_lines) == len(lines):
        print(f"No account found with username '{account_to_delete}'.")
    else:
        with open("users.txt", "w") as file:
            file.writelines(updated_lines)
        print(f"Account '{account_to_delete}' has been deleted successfully.")
    print("\nUpdated list of users:")
    with open("users.txt", "r") as file:
        print(file.read())






# edit accounts
def manage_account():
    user_role = input("Enter your role: ").lower()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt", "r") as file:
        lines = file.readlines()
    manager_authenticated = False
    for line in lines:
        role, name, passw = line.strip().split(",")
        if role.lower() == user_role and name == username and passw == password and user_role == "manager":
            manager_authenticated = True
            break
    if manager_authenticated:
        print("Authentication successful. Here is the current list of users:\n")
        print("Role, Username, Password")
        for line in lines:
            print(line.strip())
        username_to_edit = input("\nEnter the username you would like to edit: ")
        user_found = False
        updated_lines = []
        for line in lines:
            role, name, passw = line.strip().split(",")
            if name == username_to_edit:
                user_found = True
                print(f"Editing User: Role: {role}, Username: {name}, Password: {passw}")
                new_role = input("Enter new role (leave blank to keep current): ")
                new_username = input("Enter new username (leave blank to keep current): ")
                new_password = input("Enter new password (leave blank to keep current): ")
                role = new_role if new_role else role
                name = new_username if new_username else name
                passw = new_password if new_password else passw
                print("User information updated successfully.")    
            updated_lines.append(f"{role},{name},{passw}\n")
        if not user_found:
            print("User not found.")
        with open("users.txt", "w") as file:
            file.writelines(updated_lines)
    else:
        print("Access denied. Only managers can edit user information.")




# Order managment
def show_cart():
    with open("Cart.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            id, food, quantity, price = line.strip().split(",")
            print(f"ID: {id} | Food: {food} | Quantity: {quantity} | Price: {price}")

def update_order_status():
    show_cart()
    order_id = input("Enter the ID number to update the order status: ")
    new_status = input("Enter the new order status (e.g., 'Completed', 'Pending'): ")
    with open("Cart.txt", "r") as file:
        lines = file.readlines()
    updated_lines = []
    order_found = False
    for line in lines:
        parts = line.strip().split(",")
        if parts[0] == order_id:
            parts.append(new_status)
            order_found = True
        updated_lines.append(",".join(parts))
    if not order_found:
        print(f"No order found with ID: {order_id}")
        return
    with open("Cart.txt", "w") as file:
        for line in updated_lines:
            file.write(line + "\n")
    print(f"Order ID {order_id} updated to status: {new_status}")









# Add to inventory 
from datetime import datetime, timedelta

def add_to_inventory():
    with open("inventory.txt", "a") as file:
        item = input("What is the new item: ")
        quantity = float(input(f"How many {item}s are there: "))
        price_pc = float(input(f"How much does one {item} cost: "))
        total_price = quantity * price_pc
        
        
        expiration_date = (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%d")
        
       
        file.write(f"{item},{quantity},{price_pc},{total_price},{expiration_date}\n")   
        
    total_sum = 0.0
    lines = []
    with open("inventory.txt", "r") as file:
        for line in file:
            if not line.startswith("Total Price"):
                lines.append(line.strip())
                try:
                    *_, total_price = line.strip().split(',')
                    total_sum += float(total_price)
                except ValueError:
                    print("Error in line format, skipping:", line)  
    with open("inventory.txt", "w") as file:
        for line in lines:
            file.write(line + "\n")
        file.write(f"Total Price,{total_sum:.2f}\n")
    print("Inventory updated with the total price and expiration dates.")





# Remove from inventory
def delete_from_inventory(food):
    with open("inventory.txt","r") as file:
        lines = file.readlines()
        with open("inventory.txt","w") as file:
            for line in lines:
                item,quantity = line.strip().split(",")
                if item != food:
                    file.write(line)





# edit inventory
def manage_inventory():
    item_to_edit = input("Enter the item you want to edit: ")
    with open("inventory.txt", "r") as file:
        content = file.readlines()
    updated_content = []
    entry_found = False
    for line in content:
        item, quantity,price_pc, total_price = line.strip().split(",")
        if item == item_to_edit:
            new_item = input("Enter the new item: ")
            new_quantity = float(input("Enter the new quantity: "))
            new_price = float(input("Enter the new price per piece: "))
            new_total_price = new_quantity * new_price
            updated_line = f"{new_item},{new_quantity},{new_price},{new_total_price}\n"
            entry_found = True
        else:
            updated_line = f"{item},{quantity},{price_pc},{total_price}\n"
        updated_content.append(updated_line)
    if not entry_found:
        print(f"No entry found for item: {item_to_edit}")
    else:
        with open("inventory.txt", "w") as file:
            file.writelines(updated_content)
        print("File updated successfully.")



# Read feedback
def feedback():
    with open("feedback.txt","r") as file:
        content = file.readlines()
        print(content)




# Track income
def income():
    total_income = 0
    with open("Cart.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            id, food, quantity, price = line.strip().split(",")
            quantity = int(quantity)
            price = int(price)
            total_income += quantity * price 
    return total_income



# Track expenses
def expenses():
    total_expenses = 0
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 5:
                item, quantity, price, total_price, exp_date = parts
                if total_price.replace('.', '', 1).isdigit():
                    total_expenses += float(total_price)
                else:
                    print(f"Skipping invalid total_price: {total_price} in line: {line}")
            else:
                print(f"Skipping invalid line (incorrect number of fields): {line}")
    return total_expenses

def income():
    return 10000.00

def profits():
    return income() - expenses()

def display_financials():
    print(f"The total expenses are {expenses():.2f}")
    print(f"The total profits are {profits():.2f}")



