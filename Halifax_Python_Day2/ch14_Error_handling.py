def someFunction():
    print("Hello, world")
# Missing colon at the end of the function definition


try:
    division = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Try block consists of the code which may have errors
try:
    3 / 0
except Exception as e:
    print(e)

# Catch block consist of the code that is used to handle exceptions
try:
    print(newvariable)
except Exception as e:
    print(e)

# Else block consist of the code that continue the program
try:
    newvariable = 10
except Exception as e:
    print(e)
else:
    print(newvariable)

#code 1
# finally block always gets executed
try:
    newvariable = 10
except Exception as e:
    print(e)
else:
    print(newvariable)
finally:
    print('finally block')

#Code 2:# Error code
try:
    print(myvariable)
except Exception as e:
    print(e)
else:
    print(newvariable)
finally:
    print('finally block')

try:
    age = 15
    if age < 20:
        raise Exception('Below Age Exception')
except Exception as e:
    print(e)


list_1 = [2,5,7,8]
try:
    print(12/0)
    open("none_exiting.txt")
    print(list_1[4])
except IndexError as ie:
    print(ie)
except FileNotFoundError as fnfe:
    print(fnfe)
except Exception as ae:
    print("Save my Job ", ae )
finally:
    print("only for cleaning ")