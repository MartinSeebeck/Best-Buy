"""
Main module to init store CLI.
"""
import products
import store

def handle_list_products(best_buy_store):
    """Listing all available product in the store."""
    print("\n--- Available Products ---")
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("Right now there are no products in store.")
    else:
        for i, product in enumerate(all_products, 1):
            print(f"{i}. {product.show()}")

def handle_show_total(best_buy_store):
    """Showing the total quantity of all products in store."""
    total_quantity = best_buy_store.get_total_quantity()
    print(f"\nTotal products in store: {total_quantity}")

def handle_make_order(best_buy_store):
    """Guiding the user through the order process."""
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("Right now, there are no products here you can order.")
        return

    print("\n--- Placing an order ---")
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product.show()}")

    shopping_list = []
    while True:
        try:
            prompt = "Which product? (Enter the product number, type 'wrap' to finish): "
            product_choice = input(prompt)
            if product_choice.lower() == 'wrap':
                break

            product_index = int(product_choice) - 1
            if not 0 <= product_index < len(all_products):
                print("Invalid product number. Please try again.")
                continue

            quantity_choice = int(input("Which quantity do you wish to buy? "))
            if quantity_choice <= 0:
                print("The quantity needs to be above 0.")
                continue

            chosen_product = all_products[product_index]
            shopping_list.append((chosen_product, quantity_choice))
            print(f"{quantity_choice} x '{chosen_product.name}' added to the shopping cart.")

        except ValueError:
            print("Invalid entry. Please enter a number.")

    if shopping_list:
        order_total = best_buy_store.order(shopping_list)
        print(f"\nOrder successful! Total amount due: ${order_total:.2f}")

def start(best_buy_store):
    """Beginning the main loop of the shop GUI."""

    menu_options = {
        '1': handle_list_products,
        '2': handle_show_total,
        '3': handle_make_order,
    }

    while True:
        print("\n----- Store Menu -----")
        print("1. List all products in store")
        print("2. List inventory of all products in store")
        print("3. Place an order")
        print("4. Exit the store")

        choice = input("Please select an option (1-4): ")

        if choice == '4':
            print("Bye bye!")
            break

        action = menu_options.get(choice)
        if action:
            action(best_buy_store)
        else:
            print("Invalid choice. Please select an option 1 thru 4.")


def main():
    """Initializing the store and starting the program."""
    product_list = [
        products.Product("Lagavulin 16yrs old", price=54, quantity=80),
        products.Product("Ardbeg 54yrs old", price=250, quantity=50),
        products.Product("Auchentoshan Malts Of Scotland 1998 Rare Casks", price=349, quantity=30),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()