"""
Main module to init store CLI.
"""
import products
from store import Store


def main():
    # Est. a list of product instances
    product_list = [
        products.Product("Lagavulin 16yrs old 0,7l", price=52, quantity=224),
        products.Product("Ardbeg 24yrs old 1l", price=250, quantity=80),
        products.Product("Auchentoshan Malts of Scotland 1998 Rare Casks", price=349, quantity=30),
    ]

        # Est a store instance with a product list
        best_buy = Store(product_list)

        # Test the method of Store class
        print(f"Gesamtmenge im Store: {best_buy.get_total_quantity()}")

        # Get all active products
        active_products = best_buy.get_all_products()

        # Build and process order
        # E.g. Ordering 1 Lagavulin (idx 0) und 2x Ardbeg (idx 1)
        shopping_list = [(active_products[0], 1), (active_products[1], 2)]

        order_total = best_buy.order(shopping_list)
        print(f"Total amount due: {order_total}")

        # Show the actualized qty after order
        print("\nStore inventory after this order:")
        for product in best_buy.get_all_products():
            print(product.show())

        print(f"\nTotal inventory of all products after order: {best_buy.get_total_quantity()}")


    if __name__ == "__main__":
        main()