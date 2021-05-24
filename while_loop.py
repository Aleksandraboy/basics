# 03/21/21 While loop, functions
print("***incrementing the variable to reach lower boundary***")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 2

print('***decrementing the variable***')
current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -= 1

print('****Game****')
#enter color, green - 15, yellow - 10, red - 5
#other colors or somthing you loose
#q or quit is to end the game

color = None # this is global variables, need to be before while loop, because we are checking conditions
while color != 'quit' or color != 'q':
    color = input('Enter your color (green/yellow/red): ') # прошу ввести цвет (assign the volue, only inside the loop)
    color = color.lower().strip() # введенный цвет вывести маленькими буквами и удалить все лишние пробелы(strip)
    points = 0 # redeclared every for loop (повторяет каждый луп)
    if color == 'quit' or color == 'q':
        break
    if color == 'green':
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    else:
        print('Oopps, incorrect color.')
    print(f'You have {points} points.')
print('closing the game...')

#'hello guys' - count how many 'l' in the phrase 'hello guys'

count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"'number of l's is: {count}")

# h/w
# 1. how to swap 2 variable values. a=45 b=78 >> a=78 b=45
# 2. count the vowels (гласные звуки) in any phrase/sentance/word. Use enters any phrase.
# count each letter in any phrase
# find the first mostly used letter in a phrase
