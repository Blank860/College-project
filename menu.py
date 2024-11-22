# Display menu
def display_menu():
    try:
        with open("menu.txt", "r") as file:
            for line in file:
                item, price, *discount = line.strip().split(",")
                final_price = float(price) * (1 - float(discount[0])) if discount else float(price)
                discount_text = f" (Discounted: ${final_price:.2f})" if discount else ""
                print(f"{item}: ${price}{discount_text}")
    except FileNotFoundError:
        print("Menu file not found.")

