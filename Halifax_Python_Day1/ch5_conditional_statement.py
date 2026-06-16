# Example of an if statement

# Define a variable
age = 20

# Check if the person is an adult
if age >= 18:
    print("You are an adult.")
    print("You can vote.")

# Another example to check if a number is positive
number = 5
if number > 0:
    print(f"{number} is a positive number.")


# Example of an if-else statement

# Define a variable for the temperature
temperature = 30

# Check if the temperature is above 25 degrees Celsius
if temperature > 25:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

# Another example to determine if a number is even or odd
number = 4
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# Example of nested if statements

# Variables for an online store's discount policy
customer_status = "VIP"
purchase_amount = 210

# Check if the customer is a VIP
if customer_status == "VIP":
    print("Customer is a VIP.")
    # Further check if the purchase amount is over $200
    if purchase_amount > 200:
        print("You get a 20% discount.")
    else:
        print("You get a 10% discount.")
else:
    print("Regular customer.")
    # Check purchase amount for regular customers
    if purchase_amount > 200:
        print("You get a 10% discount.")
    else:
        print("You get a 5% discount.")


# Example of if-elif statement

# Variable to represent the score of a student
score = 82

# Determine the grade based on the score
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
