class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total: {self.calculate_total_price()}")

product = Product("Laptop", 1000, 3)
product.display_info()  # Виведе: Product: Laptop, Price: 1000, Quantity: 3, Total: 3000