'''
        this program tells me what fruits
        to eat each day
'''
import datetime

today = datetime.datetime.now()
print(today)

dow = today.strftime('%A')
print(dow)
fruits = ['mango','orange','pear','cherry','apple']

if dow == 'Monday':
    print(f"Eat an {fruits[0]}")
elif dow == 'Tuesday':
    print(f"Eat an {fruits[1]}")
elif dow == 'Wednesday':
    print(f"Eat an {fruits[2]}")
elif dow == 'Thursday':
    print(f"Eat an {fruits[3]}")
elif dow == 'Friday':
    print(f"Eat an {fruits[4]}")
else:
    print('Spoil yourself, you earned it')
# when if elif is beyond five consider a switch
# switch dow:
#     case "Monday":
#         print('Spoil yourself, you earned it')