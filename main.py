"""
Main module to init store CLI.
"""


import products
import store


def handle_list_products(best_buy_store):
    """Listing all available product."""
    print("\n--- Available Product ---")
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("Currently there are no products available.")
    else:
        for i, product in enumerate(all_products, 1):
            print(f"{i}. {product.show()}")

def handle_show_total(best_buy_store):
    """Showing the total of available products across store."""
    total_quantity = best_buy_store.get_total_quantity()
    print(f"\nTotal amount of available products in store: {total_quantity}")

def handle_make_order(best_buy_store):
    """Leading user through order process."""
    all_products = best_buy_store.get_all_products()
    if not all_products:
        print("There are no products at all in the store.")
        return

    print("\n--- Making an order ---")
    for i, product in enumerate(all_products, 1):
        print(f"{i}. {product.show()}")

    shopping_list = []
    while True:
        try:
            prompt = "Which product? (Enter the number, type 'done' to finish): "
            product_choice = input(prompt)
            if product_choice.lower() == 'done':
                break

            product_index = int(product_choice) - 1
            if not 0 <= product_index < len(all_products):
                print("Invalid product number. Please try again.")
                continue

            quantity_choice = int(input("Which quantity are you interested in? "))
            if quantity_choice <= 0:
                print("The quantity needs to be a positive (integer) number.")
                continue

            chosen_product = all_products[product_index]
            shopping_list.append((chosen_product, quantity_choice))
            print(f"{quantity_choice} x '{chosen_product.name}' added to shopping cart.")

        except ValueError:
            print("Invalid entry. Please enter a number.")

    if shopping_list:
        order_total = best_buy_store.order(shopping_list)
        print(f"\nOrder successful. Total amount due: ${order_total:.2f}")


def start(best_buy_store):
    """Starts the main loop of the CLI menu of the store."""

    menu_options = {
        '1': handle_list_products,
        '2': handle_show_total,
        '3': handle_make_order,
    }

    while True:
        print("\n----- Store Menu -----")
        print("1. List all products in store")
        print("2. List total amount of products in store")
        print("3. Place an order")
        print("4. End store visit")
        choice = input("Please select an option (1-4): ")
        if choice == '4':
            print("Goodbye!")
            break
        action = menu_options.get(choice)
        if action:
            action(best_buy_store)
        else:
            print("Invalid choice. Please select an option by typing numbers between 1 and 4.")


def main():
    """Initializes the store, starting the app."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    # Est a store instance with a product list
    best_buy = store.Store(product_list)
    # Test the method of Store class
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")
    # Get all active products
    active_products = best_buy.get_all_products()
    start(best_buy)


if __name__ == "__main__":
    main()


