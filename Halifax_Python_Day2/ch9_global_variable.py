# Defining a global variable
count = 10
number = 10

# Function to demonstrate global variable usage
def update_count():
    global count
    # Declare 'count' as a global variable
    count += 5
    number = 5
    print(number)
    # Modify the global variable
    print("Count inside the function:", count)

# Accessing global variable before calling the function
print("Initial global count:", count)
print("Initial global number:", number)

# Calling the function to modify the global variable
update_count()

# Accessing global variable after function call
print("Global count after function call:", count)
print("Global number after function call:", number)

