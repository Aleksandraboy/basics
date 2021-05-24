# 03/20/21 Looping through dictionary
my_car = {"brand": "Ford", "model": "Mustang", "year": "1964"}
for key in my_car:
    # print(key)
    # print(my_car[key])
    # print('******')
    print(key+":"+' '+(my_car[key]))

# do I have a model
print("*****do I have a 'model'*********")
if 'model' in my_car:
    print('yes')

print("*****using dict.values()*****")
for value in my_car.values():
    print(value)

print("*****using dict.items()*****")
for key, value1 in my_car.items():
    print(key)
    print(value1)

if 1964 in my_car.values():
    print('yes')

print("*****List sort(), sorted(list)*****")
friends = ['john', 'jane']
print(friends)
sorted_friends = sorted(friends)
print(sorted_friends)
friends.sort()
print(friends)

print("*****Sorted list*****")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
for name in sorted(favorite_languages.keys()):
    print(name,favorite_languages[name])

print('\n' + 'Exercise 6-5. Rivers:')
'''
6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
'''

rivers = {'nile': 'egypt', 'tigers':'iraq', 'amazon': 'brazil', 'mississipi':'usa'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

