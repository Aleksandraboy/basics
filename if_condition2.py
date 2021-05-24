# 03/14/2021 If statements continue
#
# num = 20
# if num >= 1 and num <= 10:
#     print(f"number is equal or greater than 1 and less than 10")
# else:
#     print(f"number is less than 1 or greater than 10")
#
# print("********")
# age = int(input('enter the visitors age: '))
# if 0 <= age <=4:
#     print('Your admission cost is $0')
# elif  4<age<18:
#     print('Your admission cost is $5')
# else:
#     print('Your admission cost is $10')
#
# print("********")
# age = int(input('enter the visitors age: '))
# price = 0
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# elif age <140:
#     price = 10
# else: print("Invalid age was entered")
# print(f"your admission cost is ${price}.")
#
# '''
# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)
# '''
#
# print("5-3. Alien Colors  #1")
# alien_color = input("enter the alien color (green/yellow/grey): ")
# if alien_color == 'green':
#     print("You just earned 5 points!")
# elif alien_color == 'yellow':
#     print("You just earned 2 points!")
# elif alien_color == 'grey':
#     print("You just earned 10 points!")
# else:
#     print("no pints, sorry, take a rest")

print('************')
friends = ["Zoya"]
if friends:
    print('good for you, can I be your friend?')
else:
    print('Go out and make some good friends')

print("****Using Multiple Lists*****")
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_toppings in requested_toppings:
    if requested_toppings in available_toppings:
        print(f"I am adding {requested_toppings}")
    else:
        print(f"Sorry we do not have {requested_toppings}")

print("**********")
# % - divide
# 10 % 5 it going to be 0.
# 15 % 10 it going to be 15 = 5*2 +5, so result going to be 5
# то есть если число делится без остатка, то будет ноль. Если число делится с остатком, покажет только остаток

# // - floor division, ignoring reminder
# 40 // 11 it going to be 3 (сколько 11 в 40)



# exercise
print("exercise")
'''
1. FussBuzz, assume user enter integer number>0
print Fuzz if the number divided by 3
print Buzz if the number divided by 5
print FuzzBuzz if the number divided by 3 and 5
'''

number = int(input('Please, enter the number > 0: '))
if number% 3==0 and number% 5==0:
    print(f"FuzzBuzz your number {number} divided by 3 and 5")
elif number % 3==0:
    print(f"Fuzz your number {number} divided by 3")
elif number % 5==0:
    print(f"Buzz your number {number} divided by 5")
else:
    print("Lets try one more time")

# H/W
# 1. Implement sum () with for loop
# 2. Double characters in a string (e.g. "abc" => "aabbcc")
# for letter in "hello"
# print('letter')
# Prove that a number is a prime
# Prove that a string is a palindrome(mom, dad, kayak, madam etc)

# websites that to practice:
# https://codingbat.com/python
# https://www.hackerrank.com/ (email: sasha, pass: boyko438114



