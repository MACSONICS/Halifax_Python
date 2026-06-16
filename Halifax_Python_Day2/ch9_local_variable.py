# Demonstrating Local Variable

def show_message():
    message = "Hello, I am a local variable!"
    # Local variable
    print("Inside the function:", message)

# Calling the function
show_message()

# Trying to access the local variable outside the function (will raise an error)
try:
    print("Outside the function:", message)
except NameError as e:
    print("Error:", e)