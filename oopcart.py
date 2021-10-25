import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

cart = []

class ShoppingCart():
    def __init__(self):
        self.add_item
        self.remove_item
        self.show_cart
        self.clear_cart

    def add_item(self):
        response = input("What would you like to add? ")
        cart.append(response)
   
    def remove_item(self):
        self.show_cart()
        response = input("what would you like to remove? ")
        cart.pop(response)

    def show_cart():
        print(cart)

    def clear_cart():
        cart.remove

class UI():
    def __init__(self):
        self.run_program
    def run_program(self):
        while True:
            response = input('What would you like to do? Add / Remove / Show / Clear / Quit ')
            if response == "add":
                self.add_item()
            if response == "remove":
                self.remove_item()
            if response == "show":
                self.show_cart()
            if response == "clear":
                self.clear_cart()
            else:
                break

run_cart=UI()
run_cart.run_program()