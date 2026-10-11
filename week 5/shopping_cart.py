class ShoppingCart:
    def __init__(self):
       
        self.items = []

    def add_item(self, name, price, quantity):
        # Add a product with its name, price, and quantity to the cart
        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def calculate_total(self):
       
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

        # Cart 1: Electronics
cart1 = ShoppingCart()
cart1.add_item("Wireless Mouse", 25.0, 2)
cart1.add_item("Keyboard", 45.0, 1)

        # Cart 2: Stationeries
cart2 = ShoppingCart()
cart2.add_item("Notebook", 3.5, 4)
cart2.add_item("Pen Pack", 5.0, 2)


print(f"Cart 1 Total: ${cart1.calculate_total()}")  # Output: $95.0
print(f"Cart 2 Total: ${cart2.calculate_total()}")  # Output: $24.0