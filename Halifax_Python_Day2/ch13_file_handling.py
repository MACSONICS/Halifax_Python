'''
Where the following mode is supported:
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
a: open an existing file for append operation. It won’t override existing data.
r+: To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It won’t override existing data.

'''
# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")

# Reading from the same file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)  # Output: Hello, World!

# Python code to create a file
file = open('knowledge.txt', 'w')
file.write("This will add a new line.")
file.write(" This will add another new line")
file.close()

file = open('knowledge.txt', 'r')
for line in file:
    print(line)

# Output when reading from file:
# This will add a new line. This will add another new line


# Python code to illustrate append() mode
file = open('knowledge.txt', 'a')
file.write(" This will append this line in the existing file.")
file.close()

file = open('knowledge.txt', 'r')
print(file.read())

