class Person:
    # Constructor to initialize name and age
    # 
    def __init__(self, n, a):
        self.name = n
        self.age = a
        # Method to display school details
    def school(self, std):
        print('The student name is: ', self.name)
        print('The age of the student is: ', self.age)
        print('The student is in', std, 'grade')

# Creating an instance of the class
boy1 = Person('William', 11)

# Calling the method to display details
boy1.school('5th')

#Code for Non-Parameterized

class Person:
    # Constructor to initialize name and age
    def __init__(self):
        self.name = 'Rob'
        self.age = 8
        # Method to display school details
    def school(self, std):
        print('The student name is: ', self.name)
        print('The age of the student is: ', self.age)
        print('The student is in', std, 'grade')

# Creating an instance of the class
boy = Person()

# Calling the method to display details
boy.school('3rd')
