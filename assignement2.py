class User:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Pizza:
    def __init__(self, size, quantity):
        self.size = size
        self.prices = {"small": 10, "medium": 12, "large": 15, "x-large": 18}
        self.quantity = quantity

    def total(self):
        price = self.prices.get(self.size.lower(), 0)
        if price == 0:
            print("Invalid pizza size. Please select Small, Medium, Large, or X-Large.")
            return 0
        if self.quantity <= 0:
            print("Error: You must order at least 1 pizza.")
            return 0
        total_price = price * self.quantity
        if self.quantity >= 3:
            total_price *= 0.85  # 15% discount for 3 or more pizzas
        return total_price

    def __str__(self):
        return f"Size: {self.size.capitalize()}, Quantity: {self.quantity}"

# Get user details
name = input("What is your name? ")
email = input("What is your email address? ")
address = input("What is your address? ")

# Create a User object
user = User(name, email, address)

# Get pizza order details
size = input("What size Pizza would you like? (Small/Medium/Large/X-Large): ")
quantity = int(input(f"One Pizza of this size is $ {Pizza(size, 1).total()}\nHow many Pizzas of this size would you like to order?: "))

# Inform the user about the discount
if quantity >= 3:
    print("You qualify for a 15% discount for ordering 3 or more pizzas.")

# Create a Pizza object
pizza = Pizza(size, quantity)

# Display order details
if pizza.total() != 0:
    print(f"You have ordered {pizza.quantity} {pizza.size.capitalize()} pizzas.")
    total_price = pizza.total()
    if total_price == pizza.total():
        print(f"Your total is, $ {total_price:.1f}.")
    else:
        print(f"Your total after discount is, $ {total_price:.1f}.")

    print(f"Order will be delivered to {user.name} at {user.address}")
    print(f"Receipt will be emailed to {user.email}")
