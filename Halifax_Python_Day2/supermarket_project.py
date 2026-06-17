class Customer:
    #constructor
    def __init__(self, em, id, username, card):
        self.email = em
        self.id = id
        self.name = username
        self.card = card
        self.shopping_basket = []

    def login(email, passwd):
        pass

    def check_out(self):
        total = 0
        for item in self.shopping_basket:
            total += item.price
        
        self.card.pay(total)
        print(f"thanks for shopping good bye")

    def add_Item_to_basket(self,product):
        self.shopping_basket.append(product)
        print(f"item {product.name} has been added to basket")

class Product:
   
    def __init__(self, n, p):
        self.name = n
        self.price = p

class Card:
   
    def __init__(self, init_balance):
        self.balance = init_balance
    
    def pay(self,amount):
        self.balance -= amount
        print(f"you made a purchase of {amount}")
        print(f"your remaining balance of your card is {self.balance}")

class SuperMarket():
    def start(self):
        card1 = Card(3000)
        cust1 = Customer("user1.email",12,"Bob",card1)

        p1 = Product("Bread",1.99)
        p2 = Product("Laptop",500)
        p3 = Product("Cofee",6.99)

        cust1.add_Item_to_basket(p1)
        cust1.add_Item_to_basket(p2)
        cust1.add_Item_to_basket(p3)

        cust1.check_out()
        
        # print(cust1.name)
        # print(cust2.name)
        # print(cust3.name)
        #cust1.login("email","123456")

our_supermarket = SuperMarket()
our_supermarket.start()