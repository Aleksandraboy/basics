# H/W from 03/20/21
print('***h/w print multiplication table 1 to 10, next line 2 to 20****')
# for num in range(1,11):
#     print(num, end=' ')
# print()
# for value in range(2, 22, 2):
#         print(value)
#
#
for num in range (1, 3):
    for value in range (1, 11):
        print ('{:3}'.format(num*value), end=' ')
    print()

# for num in range (1, 11):
#     print(num, end=' ')
for num in range (1, 3):
    for value in range (1, 11):
        print(num*value, end='\t ')
    print('\n')

# h/w 6.7 - 6.12

print('\n'+'#Exercise 6-7')
'''
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
'''
amigo = {'first_name': 'Vitaly', 'last_name': 'Ivanov', 'age': 19, 'city': 'Florance'}
amigo1 = {'first_name': 'Gosha', 'last_name': 'Petrov', 'age': 23, 'city': 'Miami'}
amigo2 = {'first_name': 'Gleb', 'last_name': 'Sidorov', 'age': 30, 'city': 'Kiev'}
people = [amigo, amigo1, amigo2]
for a in people:
    print(a)

print('\n'+'#Exercise 6-8')
'''
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
'''
orio = {'animal':'dog', 'owner':'Adam'}
patron = {'animal':'cat', 'owner':'Kirill'}
bandit = {'animal':'dog', 'owner':'Alla'}

pets = [orio, patron, bandit]

for pet in pets:
    print(pet)

print('\n'+'#Exercise 6-9')
'''
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
'''
favorite_places = {'f1': {'Masha':'Maimi'},
                   'f2': {'Vova': 'Voronok'},
                   'f3': {'Kira': 'Tai'}}

for f, favorite_place in favorite_places.items():
    print(f)
    print(favorite_place)

print('\n'+'#Exercise 6-10')
'''
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
'''
people = {
    'alexa': ['4','25'],
    'peter': ['6','44'],
    'joseph': ['7','55' ],
    'katrina': ['14','66'],
    'masha': ['20', '77']}

for name, favorite_numbers in people.items():
    print(f"My friend's ,{name.title()}, favorite numbers: ")
    for numbers in favorite_numbers:
        print(f'{numbers}')

print('\n'+'#Exercise 6-11')
''''
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the information you have stored about it.
'''
cities = {'new york': {'country': 'usa', 'population': '8 millions'},
          'london' : {'country': 'england', 'population': '9 millions'},
          'paris': {'country': 'france', 'population': '2 millions'}}
print(cities)

for citi, details in cities.items():
    print(f'\n{citi.upper()}')
    for key, value in details.items():
        print(f'{key.title()}: {value.title()}')

print('\n'+'#Exercise 6-11')
'''
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program or improving the formatting of the output.
'''
favorite_places = {'friend number 1': {'Masha':'Maimi'},
                   'friend number 2': {'Vova': 'Voronok'},
                   'friend number 3': {'Kira': 'Tai'},
                   'friend number 4': {"Rimma": 'Novgorod'}}

for friend, favorite_place in favorite_places.items():
    print(f'\n My {friend}')
    for name, place in favorite_place.items():
        print(f"{name}'s favorite place is {place}.")
