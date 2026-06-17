class Customer:
    email = 'maigbodi@gmail.com'
    id = 6
    shopping_basket = []

    def login(email, passwd):
        pass

    def check_out():
        pass

    def add_Item_to_basket(product):
        pass

class Product:
    name = 'Bread'
    price = 1.99

class Card:
    balance = 1000

    def pay(amount):
        pass

class SuperMarket():
    def start(self):
        cust1 = Customer()
        cust2 = Customer()
        cust3 = Customer()
        print(cust1.email)
        print(cust2.email)
        print(cust3.email)
        #cust1.login("email","123456")

our_supermarket = SuperMarket()
our_supermarket.start()