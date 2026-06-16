# Assigning an integer value
age = 30

# Assigning a floating-point value
temperature = 25.5

# Assigning a string
name = "Alice"

# Assigning a boolean
is_registered = True

# Printing the values of variables
print("Age:", age)
print("Temperature:", temperature)
print("Name:", name)
print("Registered:", is_registered)

# Using variables in an expression
total_score = age * 2
print("Total Score:", total_score)

# Using f-string to include variables in a formatted string
print(f"{name} is {age} years old and her registration status is {is_registered}.")



# Floating-point arithmetic
a = 5.5
b = 2.2
print("Addition:", a + b)  # Outputs 7.7
print("Multiplication:", a * b)  # Outputs 12.1


# Complex number operations
z = 1 + 2j
w = 3 - 1j
print("Complex Addition:", z + w)  # Outputs (4+1j)
print("Complex Multiplication:", z * w)  # Outputs (5+5j)

# Examples of Boolean data type usage in Python

# Boolean values
is_active = True
is_registered = False

# Print the Boolean values
print("Is active:", is_active)
print("Is registered:", is_registered)

# Using Booleans in conditional statements
if is_active:
    print("The account is currently active.")
else:
    print("The account is not active.")

# Logical operations
is_complete = True
is_successful = False

# AND operation - both need to be True
print("Both complete and successful:", is_complete and is_successful)

# OR operation - either one or both can be True
print("Either complete or successful:", is_complete or is_successful)

# NOT operation - inverts the Boolean value
print("Is not successful:", not is_successful)

# Using Booleans with other data types
number = 0
text = ""

print("Is number zero considered False?", bool(number))
print("Is empty text considered False?", bool(text))


simple_string = "Hello, Python!"
print(simple_string)

substring = simple_string[0:5]
print("Substring:", substring)



try:
    simple_string[0] = "J"
except TypeError as e:
    print(e)

# Replacing a string
simple_string = "Goodbye, Python!"
print(simple_string)

# Deleting a string
del simple_string
try:
    print(simple_string)
except NameError as e:
    print(e)

# Creating and manipulating strings
simple_string = "Hello, Python!"
print("Original String:", simple_string)

# Accessing characters
first_char = simple_string[0]
print("First character:", first_char)

# Slicing strings
substring = simple_string[0:5]
print("Substring:", substring)

# Testing immutability
try:
    simple_string[0] = "J"
except TypeError as e:
    print("Immutability error:", e)

# Replacing the string
simple_string = "Goodbye, Python!"
print("Updated String:", simple_string)

# Deleting the string
del simple_string
try:
    print(simple_string)
except NameError as e:
    print("Deletion error:", e)

my_list = [1, "Hello", 3.14, True]
print(my_list)

my_list.append("Python")
my_list.extend([False, 2.71])
print(my_list)

my_list.remove("Hello")
popped_item = my_list.pop(1)
print(my_list)
print("Popped Item:", popped_item)

first_item = my_list[0]
last_item = my_list[-1]
print("First Item:", first_item)
print("Last Item:", last_item)

sublist = my_list[1:3]
print("Sublist:", sublist)

numeric_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeric_list.sort()
print("Sorted List:", numeric_list)

# List creation and modification
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.extend(["mango", "grape"])

# Removing elements
fruits.remove("banana")
fruits.pop(2)
# Removes "grape"

# Access and slice
print("Full List:", fruits)
print("Sliced List:", fruits[1:4])

# Sorting
fruits.sort()
print("Sorted Fruits:", fruits)

my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)

# Accessing an element
print("First element:", my_tuple[0])

# Slicing a tuple
print("Slice:", my_tuple[1:3])

try:
    my_tuple = (1, 2, 3)
    # Example tuple
    my_tuple[0] = 100
    # Trying to modify the tuple
except TypeError as e:
    print(e)
     # This should print a message about tuples being immutable

# Count and Index methods
another_tuple = (1, 2, 3, 1, 3, 3, 4, 1)
print("Count of 1s:", another_tuple.count(1))
print("First occurrence of 3:", another_tuple.index(3))

# Comprehensive tuple usage example
info = ("John", "Doe", "1200 Apple St.", "Software Developer")
name, surname, address, profession = info  # Unpacking

print(f"Name: {name} {surname}")
print(f"Address: {address}")
print(f"Profession: {profession}")

# Use in a dictionary
person_info = {info: "Employee Record"}
print(person_info[info])

# Creating a dictionary
contact_info = { "John": "555-0101", "Jane": "555-0202","Doe": "555-0303"}

# Accessing dictionary values
print("John's contact:", contact_info["John"])

# Adding a new key-value pair
contact_info["Mary"] = "555-0404"
print("Updated Dictionary:", contact_info)

# Removing a key-value pair
del contact_info["Doe"]
print("Dictionary after deletion:", contact_info)

# Using get() to safely retrieve values
print("Mary's contact:", contact_info.get("Mary", "Not Found"))

# Iterating through a dictionary
for name, number in contact_info.items():
    print(f"Name: {name}, Contact Number: {number}")


# Initializing the dictionary
contact_info = {"Jane": "555-0202", "Mary": "555-0404"}

# Updating an existing value
contact_info["John"] = "555-0505"

# Merging two dictionaries
emergency_contacts = {"Police": "100", "Fire": "101"}
contact_info.update(emergency_contacts)
print("Dictionary after merging:", contact_info)

my_set = {1, 2, 3, 2, 1}
print(my_set) 
# Output will be {1, 2, 3} because duplicates are removed

my_set.remove(1)
my_set.discard(8)

# No error if '8' is not found
print(my_set)

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference:", set_a - set_b)

# Symmetric Difference
print("Symmetric Difference:", set_a ^ set_b)
