print('\n 10-1. Learning Python')
'''
Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can.... Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
'''

filepath = "C:/dev/basics/data/learning_python.txt"

print('***Reading an Entire File***')
with open(filepath) as learning_python:
    contents = learning_python.read()
    print(contents)

print('\n***Reading Line by Line***')
with open(filepath) as learning_python:
    for line in learning_python:
        print(line, end='')

print('\n\n***Making a List of Lines from a File***')
with open(filepath) as learning_python:
    lines = learning_python.readlines()
print(lines)
for line in lines:
    print(line, end = '')

print('\n 10-2. Learning C:')
'''
You can use the replace() method to replace any word in a
string with a different word.
'''
# contents = 'In Python you can change the value of a variable in your program.'
# contents.replace('Python', 'C')
with open(filepath) as learning_python:
    message = 'In Python you can change the value of a variable in your program.'
    message.replace('Python', 'C')
    print(message)
# print(contents)