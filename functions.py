# 03/21/21 functions

def greet_user(): # function always start from 'def'
    """ this is docstring, something that descride the funstion (not nesessary)"""
    print('Hello!')
greet_user() # CALL function

def greet_user_by_name(name):
    """it will say hello and use the name entered"""
    print(f"Hello, {name.title()}!")
greet_user_by_name("gregory")

def sum_numbers(num1, num2):
    print(f'sum of {num1} and {num2} is {num1+num2}')
sum_numbers(45, 874)
sum_numbers(-45, -456)

def describe_pet(pet_name, pet='cat'): # required parametr should be first, pet='cat' optional parametr
    print(f"I have a {pet} and we called him {pet_name.title()}.")
describe_pet("Hitch", "dog")
describe_pet( 'Alex', 'cat')
describe_pet(pet='dog', pet_name = "felix")
