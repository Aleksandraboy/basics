#Exception Handling - handle the situations where you expect certain type of error

filepath = "C:/dev/basics/data1/student.txt"

try:
    print('trying block started....')
    with open(filepath, 'a') as students:
        print("writing to the file...")
        students.write('Sergey')

    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)
except FileNotFoundError as err:
    print(err)
    print("Enter correct file path, check your file path.")

#print(5/5)
try:
    num=5/int(input('enter the number to divide by: '))
except ZeroDivisionError as err:
    print('You can not divide by 0')
else: # this is dependant on 'try block', if 'try block' executes, then 'else block' will be executed
    print('this is else block')
    print(f"Result of this division : {num}")
finally:
    print('I am Finally block.')


print('Program is completed!')