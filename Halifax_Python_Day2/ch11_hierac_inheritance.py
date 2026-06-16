# Define the base class
class Vehicle:
    def general_usage(self):
        print("General use: transportation")

# Define the first subclass
class Car(Vehicle):
    def specific_usage(self):
        print("Specific use: Commute to work, travel with family")

# Define the second subclass
class Truck(Vehicle):
    def specific_usage(self):
        print("Specific use: Transport goods")

# Define the third subclass
class Motorcycle(Vehicle):
    def specific_usage(self):
        print("Specific use: Road trip, racing")

# Create instances of each subclass
car = Car()
truck = Truck()
motorcycle = Motorcycle()

# Access methods from the base class
car.general_usage()  # Output: General use: transportation
truck.general_usage()  # Output: General use: transportation
motorcycle.general_usage()  # Output: General use: transportation

# Access methods from each subclass
car.specific_usage()  # Output: Specific use: Commute to work, travel with family
truck.specific_usage()  # Output: Specific use: Transport goods
motorcycle.specific_usage()  # Output: Specific use: Road trip, racing