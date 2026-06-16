# Defining the Person class
class Person:
    # Constructor to initialize name and age
    def __init__(self, n, a):
        self.name = n
        self.age = a
         # Method to display school information
    def school(self, std):
        print('The student name is: ', self.name)
        print('The age of the student is: ', self.age)
        print('The student is in', std, 'grade')

# Creating an instance of the Person class
boy1 = Person('William', 11)

# Calling the school method
boy1.school('5th')

