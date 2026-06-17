# Definition of the addition function

def addition(a, b):
    s = a + b
    print(s)
    return s

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

value1 = int(input('Provide first number: '))
value2 = int(input('Provide second number: '))
ops = input("Your Operator +, *, -, / ")

if ops == '+' :
    result = add(value1,value2)
    print(f' {value1} {ops} {value2} = {result}')
elif ops == '-' :
    result = subtract(value1,value2)
    print(f' {value1} {ops} {value2} = {result}')
    
# Calling the function
addition(2, 3)

# Lambda equivalent
my_lab_func = lambda a,b : a + b
print(my_lab_func(2,3))