#h/w 03/21/21
print('*** swap 2 variable values ****')
'''
how to swap 2 variable values. a=45 b=78 >> a=78 b=45
'''
a = 45
b = 78
print(f'a = {a} and b = {b}')
temp = a
a = b
b = temp
print(f'swaped a = {a} and swaped b = {b}')

print('\n'"*** count the vowels (гласные звуки) in any phrase/sentance/word ***")
# Count the vowels in this sentence.

vowels = 'aAeEiIoOuU'
count = 0
for v in 'Count the vowels in this sentence':
    if v in vowels:
        count = count+1
print(f"number of vowels in 'Count the vowels in this sentence' is {count}")

print('\n'"*** count each letter in any phrase ***")
# Count the vowels in this sentence.
phrase = 'Count the vowels in this sentence'
count = 0
for l in phrase:
    if l != ' ':
        count = count + 1
print(count)

# Exercise 7-8. Deli:
print('\n' + 'Exercise 7-8. Deli:')
'''
Make a list called sandwich_orders and fill it with the names of vari-
ous sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
'''
sandwich_orders = ['bagel toast', 'breakfast roll', 'egg roll']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich}.')
    finished_sandwiches.append(current_sandwich)
print(f'The following sandwiches are made:')
for finished_sandwich in finished_sandwiches:
    print(f'{finished_sandwich}')

# Exercise 7-9. No Pastrami:
print('\n' + 'Exercise 7-9. No Pastrami:')
'''
Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
'''
sandwich_orders = ['pastrami', 'bagel toast', 'pastrami','breakfast roll', 'egg roll','pastrami']
print(f"Sorry, the deli has run out of 'pastrami' sandwich.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f'Today available sandwiches:\n{sandwich_orders}')

# Exercise 7-10. Dream Vacation:
print('\n' + '7-10. Dream Vacation:')
'''
Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''
# responses = {}
# polling_active = True
# while polling_active:
#     name = input(f'What is your name? ')
#     response = input('If you could visit one place in the world, where would you go?')
#     responses[name] = response
#     repeat = input("Would you like to let another person respond? (yes/ no)")
#     if repeat == 'no':
#         break
# print(f'*** The results ***')
# for name, response in responses.items():
#     print(f'{name.title()} would like to visit {response.title()}.')

# Exercise 8-3. T-Shirt::
print('\n' + '8-3. T-Shirt:')
'''
Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
'''
def make_shirt(size, message):
    print(f'Shirt size is {size}')
    print(f"Message on the shirt is '{message}'")
make_shirt('34','Hello, everyone!')
make_shirt(message='Fuck you all', size='36')

# Exercise 8-4. Large Shirts:
print('\n' + 'Exercise 8-4. Large Shirts:')
'''
Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
'''
def make_shirt(size='Large', message='I love Python'):
    print(f"Shirt size is '{size}'")
    print(f"Message on the shirt is '{message}'")
make_shirt('Large')
make_shirt('Medium')
make_shirt('Small', 'I love NY')

# Exercise 8-5. Cities:
print('\n' + 'Exercise 8-5. Cities:')
'''
Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.
'''
def describe_city(city, country='Italy'):
    print(f"{city.title()} is in {country.title()}.")
describe_city('livorno')
describe_city('Genoa')
describe_city(country='spain', city='valencia')

