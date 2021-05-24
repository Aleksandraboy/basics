#04/01/21
# 9-6. Ice Cream Stand:
print('\n' + '9-6. Ice Cream Stand')
'''
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
'''
class Restaurant():
    """A simple attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = 'Vanilla'
        self.flavors2 = 'Chocolate'
    def describe_restaurant(self):
        print('Ice Cream Stand has next flavors '+ self.flavors + ', '+ self.flavors2)

my_restaurant = IceCreamStand ('Ise Cream House', 'IseCream')
print(my_restaurant.restaurant_name)
my_restaurant.describe_restaurant()

# 9-7. Admin:
print('\n' + '9-7. Admin')
'''9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.'''

class User():
    def __init__(self,first_name, last_name, gender, age = int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    def describe_user(self):
        print("User summary: " + "user's first name: " + self.first_name.title(), "user's last name: " + self.last_name.title(), "user's age: " + self.age, "user's gender: " + self.gender)
    def greet_user(self):
        print(self.first_name.title() + ", welcome to our website!")
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

class Admin(User):
    def __init__(self, first_name, last_name, privileges = []):
        super().__init__(self, first_name, last_name)
        self. privileges = privileges
    def show_privileges(self):
        print('An administrator’s set of privileges: ' + self.privileges)
admin = Admin ('Kira', 'First')
print(admin.first_name)
privileges = ['can add post', 'can delete post', 'can ban user']
admin.show_privileges()
admin.privileges = privileges


