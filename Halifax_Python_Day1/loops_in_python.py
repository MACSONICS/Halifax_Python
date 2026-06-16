l_1 = [5,7,9,12,15,20]
# find the average of the lst above

total = 0
for item in l_1:
    total += item

avg_value = total / len(l_1)
print(avg_value)

# dynamic driven average calc
total = 0
list_2 = []
while True:
    item = input("Please enter a number and press enter: ")
    print(type(item))
    list_2.append(item)
    total += int(item)
    choice = input('Anymore item to add Yes or No')
    if choice.lower() == 'no':
        avg_value = total / len(list_2)
        print(f"The average of {list_2} is {avg_value}")
        print('Goodbye')
        break
