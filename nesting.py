# 03/20/21
# 1. A List of Lists
# 2. A List of Dictionary
# 3. A List in a Dictionary
# 4. A Dictionary in a Dictionary

print('*** 1. A List of Lists***')
countries = ['usa', 'russia', 'spain', 'france']
cities = ['new york', 'moscow', 'barcelona', 'paris']
companies = ['level up', 'abc company', 'ola company']

customers = [countries, cities, companies]
print(customers)
print(customers[0]) # printing all countries. since countries has index '0'
print(customers[0][0]) # printing 'usa', since countries index [0] and index of 'usa' also [0]
print(customers[1][2]) # printing the 'Barcelona'


multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 10],
    [0, 1, 0]
] # multidimensional (многомерный)

print(multi_dim_nums[1][1]) # printing the number '7'

print("***Nested Loops: Looping through multidimensional list(array)***")
for column in customers: #
    print(column)
    for value in column:
        print(value)
print('******')
# for customer in customers[0][1]:
#     print(customer, end='\t')

print(customers[0][1].upper())

print('***** 2. List of dictionaries')
user_0 = {'name': 'jonh', 'age' : 25, 'city' : 'brooklyn'}
user_1 = {'name': 'jane', 'age' : 20, 'city' : 'paris'}
user_2 = {'name': 'mark', 'age' : 35, 'city' : 'tokyo'}

users = [user_1, user_0, user_2]
print(users[0])
print(users[0]['name'])
print(users[0]['age'])
print(users[0]['city'])
print(users[2]['name'])

print("******** Looping****")
for user in users:
    print(user['name'], end='||')
    print(user['age'], end='||' )
    print(user['city'])

print('***** 3. A List in a Dictionary ***** ')

countries = ['usa', 'russia', 'spain', 'france']
cities = ['new york', 'moscow', 'barcelona', 'paris']
companies = ['level up', 'abc company', 'ola company']

customers = {
    "countries" : ['usa', 'russia', 'spain', 'france'],
     "cities" : ['new york', 'moscow', 'barcelona', 'paris'],
    "companies" : ['level up', 'abc company', 'ola company']
}
print(customers['cities'])
print(customers['cities'][1]) # second element from cities

print('***** 4. A Dictionary in a Dictionary *****')
user_0 = {'name': 'jonh', 'age' : 25, 'city' : 'brooklyn'}
user_1 = {'name': 'jane', 'age' : 20, 'city' : 'paris'}
user_2 = {'name': 'mark', 'age' : 35, 'city' : 'tokyo'}

users = {
    'user_0' : {'name': 'jonh', 'age' : 25, 'city' : 'brooklyn'},
    'user_1' : {'name': 'jane', 'age' : 20, 'city' : 'paris'},
    'user_2' : {'name': 'mark', 'age' : 35, 'city' : 'tokyo'}
}
print(users)
print(users['user_0'])
print(users['user_0']['name'])

print("***keys***")
for user in users.keys():
    print(user)
    print(users[user])
print("**items***")
for username, details in users.items():
    print(username)
    print(details['name'])
print("***items(key, value)***")
for username, details in users.items():
    print(username)
    for key, value in details.items():
        print(key)
        print(value)

