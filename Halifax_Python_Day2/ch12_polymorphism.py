class Display:
    def show(self, msg1, msg2=None):
        if msg2 is not None:
            print(msg1, msg2)
        else:
            print(msg1)

# Create an instance of Display
disp = Display()

# Simulated method overloading by calling with different arguments
disp.show("Hello")             # Output: Hello
disp.show("Hello", "World")    # Output: Hello World

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark!")

# Create an instance of Dog
my_dog = Dog()

# The 'make_sound' method of Dog overrides the same method in Animal
my_dog.make_sound()  # Output: Bark!
