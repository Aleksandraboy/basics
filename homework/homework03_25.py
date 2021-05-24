#03/25/21
# Exercise 8-6. City Names:
print('\n' + 'Exercise 8-6. City Names:')
'''
Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile". Call your function with at least three city-country pairs, and print the value that’s returned.
'''
def get_formatted_city_country(city:str, country:str):
    """
    :return: a string formatted like this:"Santiago, Chile".
    """
    city_country = f"{city.title()},{country.title()}"
    return city_country.title()
print(get_formatted_city_country('levorno','italy'))
print(get_formatted_city_country('valencia','spain'))
print(get_formatted_city_country(country='france',city='paris'))

# Exercise 8-7. Album:
print('\n' + 'Exercise 8-7. Album:')
'''
Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the num-
ber of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
'''
def build_make_album(name, album_title, tracks=''):
    make_album = {'name': name, 'album': album_title}
    if tracks:
        make_album ['tracks'] = tracks
    return make_album
print(build_make_album('Beatles', 'let it be'))
print(build_make_album('rihanna', 'loud'))
print(build_make_album('queen', 'queen', tracks = '10'))

# Exercise 8-8. Album:
print('\n' + 'Exercise 8-8. Album:')
'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''
def build_make_album(artist, album_title):
    make_album = {'artist': artist, 'album': album_title}
    return make_album
while True:
    print('\n Please enter information about artist: ')
    print("(enter 'q' at any time to quit)")
    artist = input('Artist name: ')
    if artist == 'q':
        break
    album_title = input('Album title: ')
    if album_title == 'q':
        break
    make_album = build_make_album(artist, album_title)
    print(f"Here is the info you entered: {make_album}")
