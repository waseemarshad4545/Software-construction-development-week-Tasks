from abc import ABC, abstractmethod

class Product(ABC):
    """Abstract base class for all products in the store."""
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_shipping_cost(self) -> float:
        """Calculate shipping cost specific to the product type."""
        pass


class PhysicalProduct(Product):
    """Represents tangible goods that require shipping and incur weight."""
    def __init__(self, name: str, price: float, weight: float, shipping_cost: float = 5.0):
        super().__init__(name, price)
        self.weight = weight
        self.shipping_cost = shipping_cost

    def get_shipping_cost(self) -> float:
        return self.shipping_cost


class DigitalProduct(Product):
    """Represents intangible goods with no physical shipping costs."""
    def __init__(self, name: str, price: float, file_size: str):
        super().__init__(name, price)
        self.file_size = file_size

    def get_shipping_cost(self) -> float:
        # Digital goods have zero shipping costs
        return 0.0


class Order:
    """Manages the customer's selected items and cost calculations."""
    def __init__(self):
        # Stores items as a list of tuples: (Product, quantity)
        self.items = []

    def add_item(self, product: Product, quantity: int = 1):
        self.items.append((product, quantity))

    def calculate_total(self):
        """Calculates subtotal, shipping total, and grand total."""
        subtotal = 0.0
        shipping_total = 0.0
        
        for product, qty in self.items:
            subtotal += product.price * qty
            shipping_total += product.get_shipping_cost() * qty
            
        grand_total = subtotal + shipping_total
        return subtotal, shipping_total, grand_total

    def display_order_summary(self):
        print("\n" + "="*40)
        print("          ORDER SUMMARY          ")
        print("="*40)
        for product, qty in self.items:
            item_total = product.price * qty
            print(f"• {product.name} (x{qty}): ${item_total:.2f}")
            
        subtotal, shipping, total = self.calculate_total()
        print("-" * 40)
        print(f"Subtotal:         ${subtotal:.2f}")
        print(f"Shipping Cost:    ${shipping:.2f}")
        print(f"Grand Total:      ${total:.2f}")
        print("="*40 + "\n")

class PaymentMethod(ABC):
    """Abstract base class for payment strategies."""
    @abstractmethod
    def pay(self, amount: float):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str, card_holder: str):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount: float):
        masked_card = "****-****-****-" + self.card_number[-4:]
        print(f"[Payment Gateway] Processing Credit Card payment of ${amount:.2f}...")
        print(f"-> Charged successfully to card {masked_card} (Holder: {self.card_holder})")


class CashOnDeliveryPayment(PaymentMethod):
    def __init__(self, delivery_address: str):
        self.delivery_address = delivery_address

    def pay(self, amount: float):
        print(f"[Payment Gateway] Processing Cash on Delivery order for ${amount:.2f}...")
        print(f"-> Please keep exact cash ready upon arrival at: {self.delivery_address}")

if __name__ == "__main__":
    # 1. Create various products
    keyboard = PhysicalProduct(name="Mechanical Keyboard", price=79.99, weight=1.2, shipping_cost=7.50)
    ebook = DigitalProduct(name="Python Masterclass E-Book", price=24.99, file_size="15MB")
    course = DigitalProduct(name="Advanced OOP Video Course", price=99.99, file_size="2.4GB")

  
    customer_order = Order()
    customer_order.add_item(keyboard, quantity=1)
    customer_order.add_item(ebook, quantity=2)
    customer_order.add_item(course, quantity=1)

    customer_order.display_order_summary()

    _, _, total_amount = customer_order.calculate_total()
    
    selected_payment = CreditCardPayment(
        card_number="4532111122223333", 
        card_holder="Jane Doe"
    )
    
    print("Initiating Checkout...")
    selected_payment.pay(total_amount)
    print("\nThank you for your purchase! Order status: CONFIRMED.")