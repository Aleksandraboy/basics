#if statement
# if expression:
#     code here when expression is true
# else:
#     code here when expression is false

num1 = 2
num2 = 3
# if num1 < num2 :
#     print("expression is true")
# else:
#     print("expression is false")

# print("***********")
# if num1 == num2 : # comparing 2 values using ==
#     print("expression is true")
# else:
#     print("expression is false")

print("***********")
# num1_str = input("enter the num1: ")
# num1 = int(num1_str) #or next line
# num1 = int (input("enter the num1: "))
# num2 = 3
# if num1 == num2 :
#     print("expression is true")
# else:
#     print("expression is false")

# print("***second***")
# msg = True
# if msg:
#     print("expression is true")
# else:
#     print("expression is false")
#
# print("***second - 2***")
# msg = input("enter True/False: ")
# if msg:
#     print("expression is true")
# else:
#     print("expression is false")

# print("***third***")
# # msg = 0 - '0' always will be false
# msg = 5 # any other integer will be always true
# if msg:
#     print("expression is true")
# else:
#     print("expression is false")

print("***fourth***")
num = 5
if num in range(6):
    print("expression is true, and num is within the range")
else:
    print("expression is false")

num = 5
if num in range(3, 6, 2):
    print("expression is true, and num is within the range")
else:
    print("expression is false")

print("***fifth***")
num = 0
if num not in range(5):
    print("expression is true, and num is within the range")
else:
    print("expression is false")

print("***sixth***")
num = 0
if num != 0: # "!=" - not equal to
    print("expression is true, and num is within the range")
else:
    print("expression is false")

msg = input("enter the msg: ")
if msg.strip() != '':
    print(f"this message was entered: \n'{msg}'")
else:
    print("witespase was entered")

print("***Comparing the string values***")
name = input("Please enter your name: ")
if name.strip().lower() == 'john doe':
    print(f"We have missed you {name}")
else:
    print(f"Welcome {name}")

print("**** if statement with list******")
cars = ['bmw', 'ferrari', 'toyota']
if 'tesla' in cars:
    print("yes, we have tesla in stock.")
else:
    print("sorry, we don't have car in stock")

if 'sat' in 'today is saturday':
    print("yes, it is part of the string")
else:
    print("no, it is not part of the string")

print("**** if statement with lists and looping******")
cars = ['bmw', 'ferrari', 'tesla', 'toyota']
for car in cars:
    if car == 'tesla':
         print(f"This is {car.upper()}")
         break # means stop when you find 'tesla'
    else:
         print(f"current car is {car.title()}")

print('exercise: *******')
nums = [45, 4, 5, 6, 3, 10]
#print values but when you find 5 print it and print 'complited'
for num in nums:
    if num == 5:
        print(num, 'complited')
        break
    else:
        print(num, 'is not 5')

nums2 = [45, 4, 5, 6, 3, 10, 5, 123, 4, 5, 666, 5]

print('******** H/W ******')
# Count how many 5 we have in the list
nums2 = [45, 4, 5, 6, 3, 10, 5, 123, 4, 5, 666, 5]
count = 0 # it should be declared before and outside of for-loop
for num in nums2:
    if num == 5:
        count = count + 1
print(count)







