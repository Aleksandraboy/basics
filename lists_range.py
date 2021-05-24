#03/11/21 - Lists(continue)

cars = ['bmw', 'ferrari', 'tesla', 'toyota']
# making numerical list
for num in range(4):
    print(num)

# shift + F6 - shotrcut for Refactor>rename
# ctrl + Y

nums = range(4)
print(nums)

nums2 = list(range(4)) # will create list data structure
print(nums2)
for num in nums2:
    print(num)

print('range with start and stop:')
for num in range(1, 4): # результат будет 1, 2, 3 (на 1 меньше чем последняя цифра)
    print(num)

print("range with start, stop and step'2':")
for num in range(1, 10, 2): # результат через 1 ("1", 2 пропускаем, "3", 4 пропускаем) нечетные числа (odd numbers) или 1, 1+"2"=3, 3+"2"=5, 5+"2"=7
    print(num)

print("range with start, stop and step'3':")
for num in range(1, 10, 3): # результат 1, 1+"3"=4, 4+"3"=7
    print(num)

print("range even numbers from 1 to 16(include 16):")
evens = []
for num in range(2, 17, 2):
    print(num)
    evens.append(num)
    print(evens)
print(evens)

print("numbers the squares of numbers from 10 to 20:")
for num in range(10,21):
    print(num**2)

print("list of numbers the squares of numbers from 10 to 20:")
squares = list()
for num in range(10,21):
    squares.append(num**2)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

cars = ['bmw', 'ferrari', 'tesla', 'toyota']
print("********")
for car in cars:
    print(car)
    print(f"{car} index = {cars.index(car)}")

print('looping the list using index****')
for ind in range(4): # ind = index
    print(ind)
    print(f"{cars[ind]} index = {ind}")

for ind in range(len(cars)): #cars_len - любое кол-во машин в списке
    print(ind)
    print(f"{cars[ind]} index = {ind}")

#************************
# List comprehasion:
print("******************")
squares = list()
for num in range(10,21):
    squares.append(num**2)
squares = [num**2 for num in range(10,20)] # for read only now, use later
print(squares)