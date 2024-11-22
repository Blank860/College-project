# Add new recipe
def add_recipe():
    dish = input("Enter the name of the dish: ")
    ingredients = input("Enter the ingredients (separate them with commas): ").split(',')
    
    with open("recipes.txt", "a") as file:
        file.write(f"{dish}:{','.join(ingredients)}\n")
    
    print(f"Recipe for '{dish}' added successfully.")




# Delete recipe
def delete_recipe():
    dish_name = input("Enter the dish name to delete: ")
    
    with open("recipes.txt", "r") as file:
        recipes = file.readlines()
    
    updated_recipes = []
    for line in recipes:
        dish, _ = line.strip().split(":")
        if dish != dish_name:
            updated_recipes.append(line)

    with open("recipes.txt", "w") as file:
        for line in updated_recipes:
            file.write(line)
    
    print(f"Recipe for '{dish_name}' has been deleted.")




# Check inventory for ingredients
def check_inventory():
    ingredient = input("Enter the ingredient to check: ")
    
    with open("inventory.txt", "r") as file:
        for line in file:
            name, quantity = line.strip().split(",")
            if name == ingredient:
                print(f"{ingredient} available: {quantity}")
                return
    print(f"{ingredient} not found in inventory.")









# Equipment Managment
def check_equipments():
    read_only = open("equipment.txt", "r")
    for line in read_only:
        line = line.strip(",")
        print(line)

        
