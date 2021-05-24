# Lists (kind of Arrays)
# Creating a list:
nums = list()  # creating an empty list
evens = []
# Operations: create, access, add elements, remove elements, copy
num = 11
odds = [1, 3, 5, 7, 9, 457]
# index:          0  1  2  3  4  5
# negative index:-6 -5 -4 -3 -2 -1
# 5 elements, size of 'odds' list is 5
# What is the element on index 2? is is 5, since index will start with 0
friends = ['masha', 'katya', 'foma', 'ruslan']

# Access
first_friend = friends[0]
print(f"friends: {friends}")
print(f"first_friend: {first_friend}")
print(f"friends [0]: {friends[0].title()}")
print(f"friends [1]: {friends[1]}")
print(f"friends [2]: {friends[2]}")
print(f"friends [3]: {friends[3]}")
# print(f"friends [4]: {friends[4]}") # IndexError: list index out of range


print(
    f"friends [-1]: {friends[-1]}")  # Look at the right side of your list, negative index starting from the last element
print(f"friends [-3]: {friends[-3]}")
print(f"odds[-3]: {odds[-3]}")

# Adding element:
# list.append(new_element) - add new_element to the end of the list
# list.insert(index, new_element) - adds new_element on the indicated index, shifts all elements to the right
# add a friend : Obama to a friends list
friends.append('obama')
print(f"new friends list: {friends}")
friends.insert(0, 'messi')
print(f"new friends list after insert: {friends}")

# reseting the existing element, existing index should be used
friends[2] = 'anfisa'
print(f"new friends list after reset: {friends}")
# friends[7] = 'dan' # IndexError: list index out of range
# print(f"new friends list after adding new: {friends}")
# to comment do >> ctrl + /

# Remove the elements: by value, by index
friends.remove('anfisa')
# removed_one1 = friends.remove('anfisa') - this is not valid statement, since remove() does not return anything
# print(removed_one1)
print(f"new friends list after removing 'anfisa: {friends}")

removed_friends = []
removed_one = friends.pop(2)  # pop() function inform us about what it is removing
print(f"new friends list after popping index '2': {friends}")
print(removed_one)

del friends[-1]
print(f"new friends list after delete index '-1': {friends}")

# how to remove whole list
friends = []
print(f"new friends list after redefining: {friends}")

# Exercise 3-3
print('\n' + '#Exercise 3-3')
cars = ['bmw', 'ferrari', 'tesla']
print(f"I would like to own a {cars[0].upper()} car.")
print(f"I would like to own a {cars[1].title()} car.")
print(f"I would like to own a {cars[2].title()} car.")

# Exercise 3-4 Guest list
print('\n' + '#Exercise 3-4')
friends = ['masha', 'katya', 'foma', 'ruslan']
print(f'Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.')

# 03/07/21 : Organazing the list
print('\n' + '######03/07/21 : #03/07/21 : Organazing the list#######')

# sorting the list temporarily
names = ['sam', 'gary', 'kate', 'dan', 'boris']
print(names)
names.sort()
print(names)
names.sort(reverse=True)  # descending order
print(names)

# sorting the list temporarily and returning the copy of sorted list
cars = ['bmw', 'audi', 'toyota', 'subaru']
sorted_cars_asc = sorted(cars)
sorted_cars_disc = sorted(cars, reverse=True)
print(f"cars = {cars}")
print(f"sorted_cars_asc: {sorted_cars_asc}")
print(f"sorted_cars_disc: {sorted_cars_disc}")

cars.reverse()  # just reverse the original list, NO sorting
print(f"cars: {cars}")

sorted_cars_asc2 = sorted(cars)
print(sorted_cars_asc2)
sorted_cars_disc2 = sorted_cars_asc2.reverse()
print(sorted_cars_asc2)

list_size = len(cars)
print(f'list_size: {list_size}')

print(f"len('toyota'): {len('toyota')}")

# Exercise 3-8 Seeing the World
print('\n' + '#Exercise 3-8')
location = ['Paris', 'Wellington', 'Sydney', 'Tokyo', 'Davao']
print(f"Original order: {location}")
print(f"Sorted: {sorted(location)}")
print(f"Still in original order: {location}")
print(f"Sorted_ reverse: {sorted(location, reverse=True)}")
print(f"Still in original order2: {location}")
location.reverse()
print(f"Reverse original order: {location}")
location.reverse()
print(f"Reverse reversed order: {location}")
print(f"Sorted reversed order: {sorted(location)}")
location.sort(reverse=True)
print(f"Reversed sorted and reversed order: {location}")
