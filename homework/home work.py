# Whitespace to strings with Tabs and Newline
print('Python')
print('\tPython') # add TAB to your text
print('Languages:\nPython\nC\nJavaScript') # add a NEWLINE
print('Languages:\n\tPython\n\tC\n\tJavaScript') # combine TAB & NEWLINE

#Striping Whitespases

# Exercise 2-3
print('\n'+'#Exercise 2-3')
msg = "Hello Eric, would you like to learn some Python today?"
print(msg)

# Exercise 2-4
print('\n'+'#Exercise 2-4')
name = "alexa"
print(name.upper())
print(name.lower())
print(name.title())

# Exercise 2-5
print('\n'+'#Exercise 2-5')
print('\t\t\tAlbert Einstein once said, “A person who never made a \n\t\t\tmistake never tried anything new."')

# Exercise 2-6 - Repeat Exercise 2-5, but this time store the famous per-
# son’s name in a variable called famous_person. Then compose your message
# and store it in a new variable called message. Print your message.
print('\n'+'#Exercise 2-6')
famous_person = "Albert Einstein"
msg = '\t\t\t' + famous_person +' once said, "A person who never made a \n\t\t\tmistake never tried anything new."'
msg1 = f'\t\t\t{famous_person} once said, “A person who never made a \n\t\t\tmistake never tried anything new."'

print(msg1)

# Exercise 2-7
print('\n'+'#Exercise 2-7')
name = '\n\n\t\t Alexa Boyko \n\n\t\t'
print(name)
print('*****')
print(name.strip('\n''\t'))
print('*****')
print(name.lstrip('\n''\n'))
print('*****')
print(name.rstrip('\t''\t'))

# Exercise 2-8
print('\n'+'#Exercise 2-8')
num1 = 5
num2 = 3
num3 = 4
num4 = 2
num5 = 13
num6 = 24
print (f"{num1} + {num2} = {num1 + num2}")
print (f"{num5} - {num1} = {num5 - num1}")
print (f"{num3} * {num4} = {num3 * num4}")
print (f"{num6} / {num2} = {num6 / num2}")

# Exercise 2-9
print('\n'+'#Exercise 2-9')
num10 = 444
msg = 'My favorite number is  '
print(msg + str(num10))

# Exercise 3-1 Names
print('\n'+'#Exercise 3-1')
names = ['ruslan', 'tanya', 'lena', 'katya']
print(f'names: {names}')
print(f'names [0] : {names [0].title()}')
print(f'names [1] : {names [1].title()}')
print(f'names [2] : {names [2].title()}')
print(f'names [3] : {names [3].title()}')

# Exercise 3-2 Greetings
print('\n'+'#Exercise 3-2')
names = ['ruslan', 'tanya', 'lena', 'katya']
print(f'I love you my dear friend {names[0].title()}!!!')
print(f'I love you my dear friend {names[1].title()}!!!')
print(f'I love you my dear friend {names[2].title()}!!!')
print(f'I love you my dear friend {names[3].title()}!!!')

# Exercise 3-5 Changing guest list
print('\n'+'#Exercise 3-5')
friends = ['masha', 'katya', 'foma', 'ruslan']
print(f'Guests who can come: {friends}')
friends_not_come = friends.pop(0)
print(f'Guest who can not come : {friends_not_come.title()}')
friends.insert(0, 'ira')
print(f"Guests who can present: {friends}")
print(f'Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.')

# Exercise 3-6 More guests
print('\n'+'#Exercise 3-6')
msg_new = 'I have a good news, we will have a bigger dinner table, then planed before'
print(f'Hi {friends[0].title()}, {msg_new}.')
friends.insert(0, 'gosha')
print(f'New list of my guests: {friends}.')
friends.insert(2, 'klava')
print(f'New list-2 of my guests: {friends}.')
friends.append('vova')
print(f'New list-3 of my guests: {friends}.')
print(f'Hi {friends[0].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[1].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[2].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[3].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[4].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[5].title()}, I would like to invite you to family dinner tomorrow.')
print(f'Hi {friends[6].title()}, I would like to invite you to family dinner tomorrow.')

# Exercise 3-7 Shrinking Guest List
print('\n'+'#Exercise 3-7')
msg_new_1 = 'Sorry, but I can invite you for dinner.'
print(f'New msg: {msg_new_1}')
popped_guest = friends.pop(0)
print(f"{popped_guest.title()}, {msg_new_1}")
popped_guest = friends.pop(0)
print(f"{popped_guest.title()}, {msg_new_1}")
popped_guest = friends.pop(0)
print(f'{popped_guest.title()}, {msg_new_1}')
popped_guest = friends.pop(0)
print(f'{popped_guest.title()}, {msg_new_1}')
popped_guest = friends.pop(0)
print(f'{popped_guest.title()}, {msg_new_1}')
print(f"New list of my guests: {friends}")
print(f"Dear {friends[0].title()}, I would like to remind you about family dinner.")
print(f"Dear {friends[1].title()}, I would like to remind you about family dinner.")
del friends[0]
del friends[0]
print(f'My final list of guest: {friends}')

print('\n'+'***********************')
names = ['sam', 'gary', 'kate', 'dan', 'boris']
removed_guests = []

removed_guests.append(names.pop())
print(removed_guests[-1].title() + ', I am sorry that I cant invite you to the dinner.')

# Exercise with the loop
print('\n'+'#Exercise with the loop')
names = ['ruslan', 'tanya', 'lena', 'katya']
for name in names:
    print(f'I love you my dear friend {name.title()}!!!')
    print(f'Hi {name.title()}, I would like to invite you to family dinner tomorrow.' + '\n')

# Exercise 4-1 Pizzas
print('\n'+'#Exercise 4-1')
pizzas = ['classic', 'four cheeses', 'deluxe']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza.')
print("I really like pizza.")

# Exercise 4-2 Animals
print('\n'+'#Exercise 4-2')
animals = ['cat', 'dog', 'giraffe', 'horse']
for animal in animals:
    print(f"A {animal} would be a great friend.")
print("I'd like to have any of these animals.")

# Exercise home work from 03/14/21
print('\n'+'#Home work from 03/14/21')
# 1. Implement sum () with for loop
# 2. Double characters in a string (e.g. "abc" => "aabbcc")
# 3. Prove that a number is a prime
# 4. Prove that a string is a palindrome(mom, dad, kayak, madam etc)
print("1.Implement sum () with for loop.")
new_num = [1,2,3,4,5]
sum = 0
# for num in new_num:
#     sum=sum+num
#     print(sum)

numbers = [1,2,3,4,5,6]
sum=0
for num in numbers:
    sum=sum+num
print(sum)

print("2.Double characters in a string.")
# 2. Double characters in a string (e.g. "abc" => "aabbcc")
# for letter in "hello"
# print('letter')
letters = 'abc'
print(letters)
letters1 = str() # a new, empty string.
for characters in letters:
    letters1 += characters+characters
print(letters1)

print('3.Prove that a number is a prime')
# n = [ ]
# if n > 1:
#     print('false')
#     for num in range(2,n):
#         if num % n == 0:
#             print('false')
#     else:
#         print('true')

print('Prove that a string is a palindrome(mom, dad, kayak, madam etc)')
str = input("Please enter a string : ")
str1 = ""

for letters in str:
    str1 = letters + str1
print("String in reverse Order :  ", str1)

if(str == str1):
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")

print("****second version****")
string = input("Please enter a String : ")

if(string == string[:: - 1]): # string[:: – 1] returns the string in reverse order.
   print("This is a Palindrome String")
else:
   print("This is Not a Palindrome String")




# Exercise 6-2. Favorite Numbers
print('\n' + 'Exercise 6-2. Favorite Numbers')
'''
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
'''
people = {'alexa': '4', 'peter': '6', 'joseph': '7', 'katrina': '14', 'masha': '20'}
print(f"Alexa's favorite number is {people['alexa']}.")
print(f"Peter's favorite number is {people['peter']}.")
print(f"Joseph's favorite number is {people['joseph']}.")
print(f"Katrina's favorite number is {people['katrina']}.")
print(f"Masha's favorite number is {people['masha']}.")

for key in people:
    print(key.title() + ":"+' '+ (people[key]))

# Exercise 6-3. Glossary:
print('\n' + 'Exercise 6-3. Glossary:')
'''
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
a.Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
b.Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''

glossary = {'loops':'prosess of iterating going through the elements',
            'list.append':'add new element to the end',
            'pop':'function inform about what is removing',
            'range': 'generates the immutable sequence of numbers',
            'tuples': 'used to store multiple items in a single variable'}

print(f"Loops: \n{glossary['loops']}")
print(f"\nList.append: \n{glossary['list.append']}")
print(f"\nPop: \n{glossary['pop']}")
print(f"\nRange: \n{glossary['range']}")
print(f"\nTuples: \n{glossary['tuples']}")

# Exercise 6-6. Glossary:
print('\n' + 'Exercise 6-6. Polling:')
'''
6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}
favorite_languages['kate'] = 'c++'
people1 = ['jen','sarah', 'sasha']
for names in favorite_languages:
    print(f"{names.title()}, please take the favorite languages poll.")




