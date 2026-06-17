# Define the superclass
class Bird:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print(f"{self.name} can fly.")

# Define the subclass that inherits from Bird
class Parrot(Bird): # inheritance
    def speak(self):
        print(f"{self.name} can speak.")

# Create an instance of Parrot
polly = Parrot("Polly")

# Accessing methods from the superclass
polly.fly()  # Output: Polly can fly.

# Accessing method from the subclass
polly.speak()  # Output: Polly can speak.
