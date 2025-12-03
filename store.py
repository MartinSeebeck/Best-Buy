import products

class Store:
    def __init__(self, list_of_products):
        self.products = list_of_products

    def add_product(self, product):
        """Adds a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store."""
        try:
            self.products.remove(product)
        except ValueError:
            print("Error: Product not found in store.")

    def get_total_quantity(self) -> int:
        """Returns total quantity of articles in store."""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list[products.Product]:
        """Returns a list of all active products in store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list) -> float:
        """
        Processes an order to return total price.
        Variable shopping_list is a list of tuples (product, qty).
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                # Calling the buy method of the product
                price = product.buy(quantity)
                total_price += price
            except (ValueError, Exception) as e:
                print(f"Error while processing order of {product.name}: {e}")
                # Future feature? Canceling entire order here
        return total_price
