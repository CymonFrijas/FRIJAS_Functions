def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")
    print()  # Blank line for better readability

def get_order(menu):
    while True:
        try:
            choice = input("Please enter the name of the item you want to order: ").strip()
            if choice in menu:
                return choice, menu[choice]
            else:
                print("Invalid choice. Please select an item from the menu.")
        except Exception as e:
            print(f"An error occurred: {e}")

def process_payment(total_cost):
    while True:
        try:
            cash_rendered = float(input(f"Total cost is ${total_cost:.2f}. Please enter the cash rendered: $"))
            if cash_rendered >= total_cost:
                change = cash_rendered - total_cost
                return change
            else:
                print(f"Insufficient cash. You need to provide at least ${total_cost:.2f}.")
        except ValueError:
            print("Invalid input. Please enter a valid amount of cash.")

def main():
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Soda": 1.50,
        "Fries": 2.50
    }

    display_menu(menu)
    
    item, price = get_order(menu)
    print(f"You have selected: {item} - ${price:.2f}")

    change = process_payment(price)
    print(f"Thank you for your order! Your change is: ${change:.2f}")

if __name__ == "__main__":
    main()