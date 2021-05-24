# 03/28/21
# Exercise 9-1. Restaurant:
print('\n' + 'Exercise 9-1. Restaurant:')
'''9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open. Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.'''

class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
    def open_restaurant(self):
        print("We would like to inform you the restaurant " + self.restaurant_name.title() + " is now opened.")
my_restaurant = Restaurant('felisia', 'italian')
print("Restaurant name is " + my_restaurant.restaurant_name.title())
print("Restaurant cuisine type is " + my_restaurant.cuisine_type)
my_restaurant.open_restaurant()

# Exercise 9-2. Restaurant:
print('\n' + '9-2. Three Restaurants: ')
'''9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.'''

my_restaurant = Restaurant('felisia', 'italian')
print("Restaurant name is " + my_restaurant.restaurant_name.title())
print("Restaurant cuisine type is " + my_restaurant.cuisine_type)
my_restaurant.open_restaurant()

your_restaurant = Restaurant('francheska', 'polish')
print("Restaurant name is " + your_restaurant.restaurant_name.title())
print("Restaurant cuisine type is " + your_restaurant.cuisine_type)
your_restaurant.open_restaurant()

our_restaurant = Restaurant('sakura', 'japanese')
print("Restaurant name is " + our_restaurant.restaurant_name.title())
print("Restaurant cuisine type is " + our_restaurant.cuisine_type)
our_restaurant.open_restaurant()

# Exercise 9-3. Users::
print('\n' + '9-3. Users: ')
'''
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
'''

# class User():
#     def __init__(self,first_name, last_name, gender, age = int):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.gender = gender
#     def describe_user(self):
#         print("User summary: " + "user's first name: " + self.first_name.title(), "user's last name: " + self.last_name.title(), "user's age: " + self.age, "user's gender: " + self.gender)
#     def greet_user(self):
#         print(self.first_name.title() + ", welcome to our website!")
# user_first = User('willi', 'rose', 'male', '15')
# print("User summary:" + '\n'+
#       "user's first name: " + user_first.first_name.title() + '\n'+
#       "user's last name: " + user_first.last_name.title() + '\n'+
#       "user's gender: " + user_first.gender + '\n'+
#       "user's age: " + user_first.age)
# user_first.greet_user()
# user_second = User('greg', 'pattern', 'male', '24')
# print("User summary:" + '\n'+
#       "user's first name: " + user_second.first_name.title() + '\n'+
#       "user's last name: " + user_second.last_name.title() + '\n'+
#       "user's gender: " + user_second.gender + '\n'+
#       "user's age: " + user_second.age)
# user_second.greet_user()

class User:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    def describe_user(self):
        'print summery of user info'
        print(self.first_name.title())
        print(self.last_name.title())
        print(self.gender)
        print(self.age)
    def greet_user(self):
        'Print personalized greeting to a user'
        print(f'Hello {self.first_name.title()}, nice to see you!')
# create several instance and use both methods for each
user1 = User ('fred', 'broun', 'male', '40')
user2 = User ('gladis', 'white', 'female', '24')

user1.describe_user()
user2.describe_user()

user1.greet_user()
user2.greet_user()


# 9-4. Number Served:
print('\n' + '9-4. Number Served:')
'''
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any num-
ber you like that could represent how many customers were served in, say, a
day of business.
'''
class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def number_of_customers(self):
        print("This restaurant has served " + str(self.number_served) + " people daily.")
    def set_number_served(self, number_of_people):
        self.number_served = number_of_people
    def increment_number_served(self, number_of_people):
        self.number_served += number_of_people

my_restaurant = Restaurant('felisia', 'italian')
print("Restaurant name is " + my_restaurant.restaurant_name.title())
my_restaurant.number_of_customers()

my_restaurant.number_served = 45
my_restaurant.number_of_customers()

my_restaurant.set_number_served(50)
my_restaurant.number_of_customers()

my_restaurant.increment_number_served(13)
my_restaurant.number_of_customers()

# 9-5. Login Attempts:
print('\n' + '9-5. Login Attempts:')
'''
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
'''
class User():
    def __init__(self,first_name, last_name, gender, age = int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0
    # def number_of_login_attempts(self):
    #     print (str(self.login_attempts))
    def increment_login_attempts(self):
        print("incrementing the value by 1...")
        self.login_attempts += 1
    def reset_login_attempts(self):
        print("resetting the value to 0...")
        self.login_attempts = 0
user_first = User('willi', 'rose', 'male', '15')
print("User summary:" + '\n'+
      "user's first name: " + user_second.first_name.title() + '\n'+
      "user's last name: " + user_second.last_name.title() + '\n'+
      "user's gender: " + user_second.gender + '\n'+
      "user's age: " + user_second.age)
user_first.increment_login_attempts()
user_first.increment_login_attempts()
user_first.increment_login_attempts()
user_first.increment_login_attempts()
print ("Login attempts: ", user_first.login_attempts)
user_first.reset_login_attempts()
print ("Login attempts: ", user_first.login_attempts)





