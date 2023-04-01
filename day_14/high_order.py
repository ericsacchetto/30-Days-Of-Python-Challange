import string
from functools import reduce
"""
map() function:
Takes a function and an iterable
Returns iterable of the function applied to each element

filter() function:
Takes a function and an iterable
Returns iterable of the function True results

reduce() function:
Takes a function and an iterable
Returns only one value
"""

"""
High Order Function:
A function that encompass other functions
either by receiving as parameter or 
returning another function.

Closure:
Encapsulating a function and returning to
the outer function

Decorator:
Implement a function to another function
without changing its structure
"""

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def call_map(x):
    return x * x

def call_filter(y):
    if (y ** 3) < 100:
        return True
    else:
        return False

def call_reduce(z, w):
    return z - w

map_result = map(call_map, numbers)
print(list(map_result))

filter_result = filter(call_filter, numbers)
print(list(filter_result))

reduce_result = reduce(call_reduce, numbers)
print(reduce_result)

# for country in countries:
#     print(country)
#
# for name in names:
#     print(name)
#
# for number in numbers:
#     print(number)

def item_upercase(i):
    return i.upper()

map_upercase = map(item_upercase, countries)
print(list(map_upercase))

def square(s):
    return s ** 2

map_square = map(square, numbers)
print(list(map_square))

map_name_upercase = map(item_upercase, names)
print(list(map_name_upercase))

def land_filter(j):
    if 'land' in j:
        return False
    else:
        return True

filter_land = filter(land_filter, countries)
print(list(filter_land))

def six_characters(o):
    if len(o) == 6:
        return False
    else:
        return True

filter_six_result = filter(six_characters, countries)
print(list(filter_six_result))

def six__more_characters(p):
    if len(p) >= 6:
        return False
    else:
        return True

filter_more_result = filter(six__more_characters, countries)
print(list(filter_more_result))


def filter_e(u):
    if u[0] == 'E':
        return False
    else:
        return True

e_result = filter(filter_e, countries)
print(list(e_result))


chain = filter(filter_e, map(item_upercase, countries))
print(f"Chain functions: {list(chain)}")

def to_string(s):
    return str(s)

string_list = map(to_string, numbers)
print(list(string_list))


def sum_all(x, y):
    return x + y

sum_list = reduce(sum_all, numbers)
print(sum_list)

def sum_countries(c, d):
    return str(c + ", ") + d

msg_countries = reduce(sum_countries, countries) + " are north European countries"
print(msg_countries)

def starts_with(c):
    if c[0] == 'B':
        return True
    else:
        return False

from data import countries
start_b = filter(starts_with, countries.countries)
print(list(start_b))

result_a = {}
for let in string.ascii_uppercase:
    result_a[let] = list(filter(lambda x: x[0] == let, countries.countries))

print(result_a)


def get_first_ten(o):
    return o[:10]

def get_last_ten(y):
    return y[len(y) - 10: len(y)]

print(f"Ten first: {list(get_first_ten(countries.countries))}")
print(f"Last ten: {list(get_last_ten(countries.countries))}")
