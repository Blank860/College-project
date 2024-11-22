from importlib.resources import open_binary
from random import choice
from re import split
import re

# Manage account
def manage_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("users.txt","r") as file:
        lines = file.readlines()
        with open("users.txt", "w") as file:
            for line in lines:
                role,name,passw = line.strip().split(",")
                if name == username and passw == password:
                    print("login clear")
                    choice = input("Type'username' or 'password' to edit: ").strip().lower()
                    if choice == "username":
                        name = input("Enter new username: ")
                    elif choice == "password":
                        passw = input("Enter new password: ")
                    else:
                        print("Invalid Choice.")
                file.write(f"{role},{name},{passw}\n")




def id():
    with open("Cart.txt","r") as file:
        lines = file.readlines()
        print(lines)
        if len(lines) == 0:
            return 1
        else:
            line = lines[len(lines) - 1].strip().split(",")
            id = int(line[0])
            id += 1
            return id





# Add to Cart
def add_to_cart():
    with open("menu.txt", "r") as file:
        menu = {line.strip().split(",")[0]: int(line.strip().split(",")[1]) for line in file.readlines()} 
    item = input("What would you like to add to your cart: ")
    if item not in menu:
        print(f"Sorry, {item} is not available in the menu.")
        return
    quantity = int(input(f"How many {item}s would you like: "))
    price = menu[item]
    with open("Cart.txt", "a") as file:
        new_id = id()
        file.write(f"{new_id},{item},{quantity},{price}\n")
    
    print(f"{item} has been added to your cart.")






# Remove from Cart
def remove_from_cart():
    item_name = input("What would you like to remove: ")
    updated = False
    with open("Cart.txt", "r") as file:
        lines = file.readlines()
    with open("Cart.txt", "w") as file:
        for line in lines:
            item, quantity, price = line.strip().split(",")
            if item == item_name:
                updated = True
            else:
                file.write(line)
    if updated:
        print(f"Item '{item_name}' has been removed from the cart.")
    else:
        print(f"Item '{item_name}' not found in the cart.")








# Modify cart
def modify_item_in_cart():
    with open("menu.txt", "r") as file:
        menu = {line.strip().split(",")[0]: int(line.strip().split(",")[1]) for line in file.readlines()}
    with open("Cart.txt", "r") as file:
        cart_items = file.readlines()
    if not cart_items:
        print("Your cart is empty.")
        return
    print("Your current cart items:")
    for idx, line in enumerate(cart_items):
        print(f"{idx + 1}. {line.strip()}")
    item_number = int(input("Enter the number of the item you want to modify: ")) - 1
    if item_number < 0 or item_number >= len(cart_items):
        print("Invalid selection.")
        return
    selected_item = cart_items[item_number].strip()
    old_item, old_quantity, old_total_price = selected_item.split(",")
    old_quantity = float(old_quantity)
    old_total_price = float(old_total_price)
    new_item = input(f"Enter the new food item (or press enter to keep {old_item}): ")
    if new_item:
        if new_item not in menu:
            print(f"Sorry, {new_item} is not available in the menu.")
            return
        price = menu[new_item]
    else:
        new_item = old_item
        price = menu[old_item]
    new_quantity = int(input(f"Enter the new quantity for {new_item}: "))
    new_total_price = new_quantity * price
    updated_item = f"{new_item},{new_quantity},{new_total_price:.2f}\n"
    cart_items[item_number] = updated_item
    with open("Cart.txt", "w") as file:
        file.writelines(cart_items)
    print(f"Item has been updated to {new_item} with {new_quantity} quantity and a total price of {new_total_price:.2f}.")





# Feedback
def feedback():
    with open("users.txt","r") as file:
        lines = file.readlines()
        input_role = input("Whats your role: ").lower()
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for line in lines:
            role,name,passw = line.strip().split(",")
            if name == username and passw == password:
                if input_role == "customer":
                        thoughts = input("Share your feedback with us: ")
                        with open("feedback.txt","a") as feedback_file:
                            feedback_file.write(f"{thoughts}\n")
                    
