# 03/13/21
#Working with the part of the list

cars = ['bmw', 'ferrari', 'tesla', 'toyota']
for car in cars:
    print(f"the car is: {car}")

# slice of the list list_name[start:stop] - start is inclusive, stop is exclusive values
# values: list_name[start], list_name[start+1],..., list_name[stop-1]
print("Slice of the list:")
for car in cars[1:3]:
    print(f"the car is: {car}")

print("****second****")
for car in cars[0:3]:  # if you didn't put anything it means start from '0', you can put '0' or not
    print(f"the car is: {car}")

print("****third*****")
for car in cars[2:]:  # if you want include until the end of the list[2:] the last one will not include
                     # if you want to see whole list[:]
    print(f"the car is: {car}")

print("****fourth*****")
for car in cars[2:10]:  # no out of range error
    print(f"the car is: {car}")

print("****linking*****")
cars2 = cars
print(f"cars: {cars}")
print(f"cars2: {cars2}")
cars.append('bmw2')
print(f"cars after update: {cars}")
print(f"cars2 after update: {cars2}")

print("****coping*****")
cars3 = cars[:]
print(f"cars: {cars}")
print(f"cars3: {cars3}")
cars.append('honda')
print(f"cars after update: {cars}")
print(f"cars3 after update: {cars3}")

#Exercise 4-10: Slicing
print("****Exercise 4-10: Slicing****")
print(f"The first three items in the list are: {cars[:3]}")
print(f"Three items from the middle of the list are:{cars[2:-1]}")
print(f"The last three items in the list are:{cars[3:]}")

#Lists can be modified (mutable - изменяемый)
#Tuples - data structure similar to list but can not be modified (immutable - неизменный)
cars_t = ('bmw', 'ferrari', 'tesla', 'toyota')
print(f"first value is: {cars_t [0]}")
cars[0] = 'ford' # this is possible since cars is the list data structure
#cars_t[0] = 'ford' # this is not possible since the cars_t is tuple
print(f"cars_t tuple: {cars_t}")

cars_t = ('tesla', 'toyota', 'bmw')
print(f"cars_t tuple: {cars_t}")