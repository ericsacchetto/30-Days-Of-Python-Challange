import math
import sys

print("Exercise 1:")
print(sys.version)

num1 = 3
num2 = 4

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 % num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)

print("Eric")
print("Sacchetto")
print("Brasil")
print("I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("Eric"))
print(type("Sacchetto"))
print(type("Brasil"))

print("Exercise 3:")
eg_int = 5
eg_float = 7.15
eg_compl = 1+2j
eg_str = "My name"
eg_bool = True
eg_list = ['banana', 'apple', 'peach']
eg_tup = ('Auckland', 'Hamilton')
eg_set = {1, 2, 5, 7, 9, 16}
eg_dict = {'name': 'Eric'}

print(f"{eg_int} type: {type(eg_int)}")
print(f"{eg_float} type: {type(eg_float)}")
print(f"{eg_compl} type: {type(eg_compl)}")
print(f"{eg_str} type: {type(eg_str)}")
print(f"{eg_bool} type: {type(eg_bool)}")
print(f"{eg_list} type: {type(eg_list)}")
print(f"{eg_tup} type: {type(eg_tup)}")
print(f"{eg_set} type: {type(eg_set)}")
print(f"{eg_dict} type: {type(eg_dict)}")

print("Exercise 3: ")
p1 = [2, 3]
p2 = [10, 8]

dist = math.sqrt(((p1[1]-p1[0])**2) + ((p2[1]-p2[1])**2))
print(dist)
