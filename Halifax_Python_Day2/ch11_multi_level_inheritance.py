
# Define the base class
class MusicalInstrument:
    def has_strings(self):
        print("This is a string instrument.")

# Define the first derived class
class Guitar(MusicalInstrument):
    def number_of_strings(self):
        print("This guitar has six strings.")

# Define the second derived class from the first derived class
class ElectricGuitar(Guitar):
    def electrify(self):
        print("This guitar is electric.")

# Create an instance of ElectricGuitar
my_guitar = ElectricGuitar()

# Access methods from the base class
my_guitar.has_strings()  # Output: This is a string instrument.

# Access method from the first derived class
my_guitar.number_of_strings()  # Output: This guitar has six strings.

# Access method from the second derived class
my_guitar.electrify()  # Output: This guitar is electric.

