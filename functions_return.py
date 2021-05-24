# 03/25/21 Functions with return statment
def get_formatted_name(first_name: str, last_name: str):
    """Return a full name, neatly formatted."""
    name = f"{first_name.title()} {last_name.title()}"
    return name.title()
print(get_formatted_name('jimi', 'hendrix'))
print(get_formatted_name('alexa', 'tamarina'))

# getter, setter functions
def get_desc_of_what_you_want_to_get():
    #logic
    return

def set_desc_of_get_desc_of_what_you_want_to_update():
    pass

def get_list_of_even_numbers(num: int):
    """
    this function return list of even numbers up to num(inclusive)
    """
    #return [range(2,num+1, 2)] # there are two ways to create a list of numbers
    return list(range(2, num+1, 2))
print(get_list_of_even_numbers(20))

def print_usernames(users: list):
    for user in users:
        print(user)
print_usernames('karim')
print_usernames(['karim'])


