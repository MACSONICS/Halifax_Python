class Car:
    # Class attributes
    wheels = 4 
    headlights = 2
    # Method to display the speed of the car
    def speed(self):
        print("The car's speed is 120 km/h")
        # Method to display the mileage of the car
    def mileage(self):
        print("The car's mileage is 15 km/l")



# Creating an object of the class
my_car = Car()

# Accessing class attributes
print("Number of wheels:", my_car.wheels)
print("Number of headlights:", my_car.headlights)

# Calling class methods
my_car.speed()
my_car.mileage()

# Creating an instance of the Car class named 'land_rover'
land_rover = Car()

# Accessing class attributes
print("Number of wheels:", land_rover.wheels)
print("Number of headlights:", land_rover.headlights)

# Calling methods for the land_rover instance
land_rover.mileage()
land_rover.speed()

