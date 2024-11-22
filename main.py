import account
import manager
import chef
import cashier
import customer

def show_manager_menu():
    print("\nManager Options:")
    print("1. Delete Account")
    print("2. Manage Accounts")
    print("3. Manage Inventory")
    print("4. View Feedback")
    print("5. View Income and Expenses")
    choice = input("Choose an option: ")
    if choice == "1":
        username = input("Enter the account username to delete: ")
        manager.delete_account()
    elif choice == "2":
        manager.manage_account()
    elif choice == "3":
        manager.manage_inventory()
    elif choice == "4":
        manager.feedback()
    elif choice == "5":
        print(f"Income: {manager.income():.2f}")
        print(f"Expenses: {manager.expenses():.2f}")
        print(f"Profits: {manager.profits():.2f}")

def show_chef_menu():
    print("\nChef Options:")
    print("1. Add Recipe")
    print("2. Delete Recipe")
    print("3. Check Inventory")
    print("4. Manage Equipments")
    choice = input("Choose an option: ")
    if choice == "1":
        dish = input("Enter the recipe name: ")
        ingredients = input("Enter the ingredients (comma-separated): ")
        chef.add_recipe(dish, ingredients.split(","))
    elif choice == "2":
        dish_name = input("Enter the recipe name to delete: ")
        chef.delete_recipe(dish_name)
    elif choice == "3":
        ingredient = input("Enter the ingredient to check: ")
        chef.check_inventory(ingredient)
    elif choice == "4":
        chef.check_equipments()

def show_cashier_menu():
    print("\nCashier Options:")
    print("1. Add Discount")
    print("2. Remove Discount")
    print("3. Modify Discount")
    print("4. Generate Bill")
    choice = input("Choose an option: ")
    if choice == "1":
        item = input("Enter the item name: ")
        discount_rate = float(input("Enter discount rate (%): "))
        cashier.add_discount(item, discount_rate)
    elif choice == "2":
        item = input("Enter the item name: ")
        cashier.delete_discount(item)
    elif choice == "3":
        item = input("Enter the item name: ")
        new_rate = float(input("Enter the new discount rate (%): "))
        cashier.modify_discount(item, new_rate)
    elif choice == "4":
        username = input("Enter the username for the bill: ")
        cashier.generate_bill(username, "Cart.txt", "users.txt", "bill.txt")

def show_customer_menu():
    print("\nCustomer Options:")
    print("1. Manage Account")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. Modify Cart")
    print("5. Provide Feedback")
    choice = input("Choose an option: ")
    if choice == "1":
        customer.manage_account()
    elif choice == "2":
        customer.add_to_cart()
    elif choice == "3":
        item_name = input("Enter the item to remove: ")
        customer.remove_from_cart(item_name)
    elif choice == "4":
        customer.modify_item_in_cart()
    elif choice == "5":
        customer.feedback()

def main():
    users_file = "users.txt"

    print("Press 1 to create a new account or press 2 to login:")
    choice = input()

    if choice == '1':
        account.create_account(users_file)
    elif choice == '2':
        role = account.login(users_file)
        while True:
            if role == "Manager":
                show_manager_menu()
            elif role == "Customer":
                show_customer_menu()
            elif role == "Chef":
                show_chef_menu()
            elif role == "Cashier":
                show_cashier_menu()
            else:
                print("Login failed.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

