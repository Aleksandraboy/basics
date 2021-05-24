# 03/18/21 Dictinary - java(HashMap, HashTable)

# Key/value pair data structure, since every element comes as (key: value)
# Create. access, modify (add/remove/ update elements)
# Looping this data structure
# some mostly used builtin functions

my_friend = {}  # this is empty dictionary
my_house = dict() # this is empty dictionary

my_car = {"brand": "Ford", "model": "Mustang", "year": "1964"}
print(my_car)
print(my_car["brand"])

print('price is added******')
my_car['price'] = 125000.00
print(my_car)

# updating the value in dictionary
print('updating the value in dictionary')
print('price was updating*****')
my_car['price'] = 1200000.00
print(my_car)

# removing the values from dictionary
print("****element with 'key' year was removed")
del my_car['year']
print(my_car)

print("Exerecise 6-1: *****")
'''
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
'''
amigo = {'first_name': 'Vitaly', 'last_name': 'Ivanov', 'age': 19, 'city': 'Florance'}
print(amigo['first_name'])
print(amigo['last_name'])
print(amigo['age'])
print(amigo['city'])
