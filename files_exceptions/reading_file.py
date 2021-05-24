#04/04/21 Reading a file

# filepath = "C:\\dev\\basics\\data\\students.txt" # absolute path to project for windows only!!! (\\)
filepath = "C:/dev/basics/data/students.txt"

#*********READING FROM FILE*************

# Reading an Entire File
# with open(filepath) as students:
#     contents = students.read()
#     print(contents)

# Reading Line by Line
# with open(filepath) as students:
#      for line in students:
#          print(line, end='')

# Making a List of Lines from a File
# with open(filepath) as students:
#     lines = students.readlines()
#
# print(lines)
# print(lines[0]) # what is the first line [0]
# print(lines[-1]) # what is the last line [-1]
#
# for line in lines:
#     print(line, end = '')

#****************WRITING TO AN EMPTY FILE************

# with open(filepath, 'a') as students: # 'a' is for append (добавить), that appends the value to the file content, 'w' is for write that truncate (обрезать) the file and add new content
#     print("writing to the file...")
#     students.write('Sergey')
#
# with open(filepath, 'r') as students:
#     lines = students.readlines()
#     print(lines)

