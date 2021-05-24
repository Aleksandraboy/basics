# 03/25/21
print(f'\n' "Exercise 8-2. Favorite Book: ")
'''
8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title. The function should print a message, such as One of my favorite books is Alice in Wonderland. Call the function, making sure to include a book title as an argument in the function call.
'''
def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book('Alice in Wonderland')

print(f'\n' "Function that prints multiplication of numbers:")
def mult_numbers(num1,num2):
    print(f"Multiplication of {num1} and {num2} is {num1*num2}")
mult_numbers(3, 5)

# swapping the values without using new variable
num1 = 'number one'
num2 = 'number two'
print(num1, num2)
num1, num2=num2, num1 # swapping the values without using new variable
print(num1, num2)

# Primitive data type: float, integer, string, boolean
# Data structure: dictionary ({}), list([]), tuples(())