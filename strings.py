# 03/04/2020  String(str)

fullname = "john doe"
msg = "we are looking at string functions in python"

# Functions available for Strings
print(fullname)
print(fullname.upper())
print(fullname.lower())
print(fullname.title())
print(msg.replace('.', '!!!!!').title())
print(msg.replace('python', 'java'))

# Concatenation
msg1 = fullname.title() + ", " + msg
print(msg1)
msg2 = "Hello, " + fullname.title() + "!"
print(msg2)


# Working with Whitespaces in strings: \t (tab), \n (move to a new line)
print(fullname.upper() +"\t, " + msg)
msg2 = fullname.title() + "\n\n\t" + msg
print(msg2)
print(msg2.replace('\n\t', ''))
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
#String.strip - removes leading and preceding whitespace(удаляет пробелы слева и справа)
print(msg3 +"!!!!")
print(msg3.strip() + "!!!")

#fstring
msg3 = '\n\t\t\t' + fullname.upper() + ", " + msg
msg4 = f"\n\t\t\t {fullname.upper()}, {msg}"
print("fstring")
print(msg4.strip() + "!!!")

print('Integers: ************')
num = 456
num2 = 502
print(f"num + num2 = {num + num2}")
print(f"num - num2 = {num - num2}")
print(f"num * num2 = {num * num2}")
print(f"num / num2 = {num / num2}")

# str(expresion) - this will convert the data type to string
print("Value of num is : " + str(num))
print("num + num2 = " + str (num + num2))

num3 = "753" # it is a string(str) not integer(int)
print(f"num + num3 = {num + int(num3)}")

print(f"3**2 = {3**2}") # exponent

num4 = "45.55"
print(f"num + num4 = {num + float(num4)}")

print (int(45.4988))













