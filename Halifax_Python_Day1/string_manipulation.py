my_str = 'This is string manipulation 8 k'
print(my_str.upper())
print(my_str) # string are immutatable
my_str = my_str.upper() # replace or reassign
print(my_str) # now all uppercase
#length of a string
print(len(my_str)) # same as below

str_size = len(my_str)
print(str_size)

print(my_str[3]) # the fourth item
print(my_str[-1]) # the last item

str_value = 'Hello ' + 'World'
print(str_value)
del str_value
print(str_value)