

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self):
        item = input('Input item to add to cart: ')
        self.items.append(item)
        print(f"Added {item} to cart")

    def debit_item(self):
        out_product = input('Input item to remove from cart: ')
        if out_product in self.items:
            self.items.remove(out_product)
            print(f"Debited {out_product} from cart")
            print(f'Remaining items: {self.items}')
            if not self.items:
                self.delete_cart()
            else:
                user_input = input("Do you want to delete the cart? (Y/N) ")
                if user_input.lower() == "y":
                    self.delete_cart()
        else:
            print(f"{out_product} not found in cart")

    def delete_cart(self):
        self.items = []
        print("Deleted all items from cart")

# Create an object of the ShoppingCart class
cart = ShoppingCart()

# Call the add_item method to add items to the cart
cart.add_item()
cart.add_item()
cart.add_item()

# Call the debit_item method to remove an item from the cart
cart.debit_item()

# Call the delete_cart method to remove all items from the cart
cart.delete_cart()
