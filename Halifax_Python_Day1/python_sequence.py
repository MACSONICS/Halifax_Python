# strings, list, tuple
list_1 = [] # this is an empty
list_2 = list() # same as above
print(type(list_1))
print(list_1)

fruit = input('Enter your first fruit and press enter: ')
list_1.append(fruit)
print(list_1)
'''
 
 
 multi line comment
'''
four_more_fruits = ['mango','orange','pear','cherry']
list_1.append(four_more_fruits)
print(list_1) # not what you expected
list_1.extend(four_more_fruits)
print(list_1)
print(list_1[-1])