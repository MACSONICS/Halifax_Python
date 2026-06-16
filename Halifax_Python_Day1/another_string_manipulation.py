list_of_fruits = ['apple','pear','grape','pineapple','orange']
print(list_of_fruits[0]) #apple the first
print(list_of_fruits[-1]) #orange the last

# list slicing or subsets
print(list_of_fruits[0:3]) #same as below
print(list_of_fruits[:3])

print(list_of_fruits[-4:-2])#same as below using positive index
print(list_of_fruits[1:3])
print(list_of_fruits[-3:-1])

student_data = ['Bob',25,['Blue','Red','Yellow',[1,3,5,7]]]
print(student_data[2])
print(student_data[2][3])
print(student_data[2][3][2])
# remove, sort, reverse
print(student_data[::-1])# speacial reverse
