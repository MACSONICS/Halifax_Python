for i in range(5):
    print(i)

count = 0
while count < 5:
    print(count)
    count += 1

'''
Code Explanation:

The while loop continues as long as count is less than 5.Inside the loop, it prints the current value of count and then increments count by 1. When count reaches 5, the condition count < 5 becomes false, and the loop exits.

'''

for num in range(10):
    if num == 3:
        continue # skip the print for 3
        if num == 8:
            break  # break the loop when num is 8
        print(num)
    else:
        print("Loop completed successfully!")