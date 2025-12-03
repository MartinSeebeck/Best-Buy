'''
In products.py's init, get_quantity returns int but the spec says float—change to return float(self.quantity) for precision, though it works as-is for whole numbers.
'''


class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Name may not be empty.")
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity may not be negative.")
        self.name = name
        self.price = float(price)
        self.quantity = float(quantity)
        self.active = True


    def get_quantity(self) -> int:
        """Retrieves the quantity of product."""
        return int(self.quantity)


    def set_quantity(self, quantity):
        """Defines the quantity of product."""
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """Checks whether it is active."""
        return self.active


    def activate(self):
        """Activates product."""
        self.active = True


    def deactivate(self):
        """De-activates product."""
        self.active = False


    def show(self):
        """Returns product details as string."""
        return f"{self.name}, Price: {self.price}, Qty: {int(self.quantity)}"


    def buy(self, quantity) -> float:
        """Enables buy of defined quantity of product."""
        if not self.active:
            raise Exception("The product is not active.")
        if quantity <= 0:
            raise ValueError("The quantity must always be a positive number.")
        if quantity > self.quantity:
            raise ValueError("Not sufficient quantity of product in inventory.")
        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)
        return total_price
