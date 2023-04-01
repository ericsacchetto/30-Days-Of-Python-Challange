from math import sqrt


def add_two_numbers(num1, num2):
    sum = num1 + num2
    return sum


print(f"Sum of 2 and 4: {add_two_numbers(2, 4)}")


def circle_area(radius):
    area = 3.14 * radius ** 2
    return area


print(f"Area of circle r = 12: {circle_area(12)}")


def add_all_nums(*nums):
    sum_all = 0
    for i in nums:
        if type(i) == int or type(i) == float:
            sum_all += i
        else:
            print(i + " is not a valid number")
    return sum_all


print(f"Sum of all numbers: {add_all_nums(1, 2, 3, 4, 5, 'Six')}")


def convert_celsius_to_fahrenheit(celsius):
    temp_inF = (celsius * (9 / 5)) + 32
    return temp_inF


print(f"30 Celsius in Fahrenheit: {convert_celsius_to_fahrenheit(30)}")


def check_season(month):
    month_lower = month.lower()
    if month_lower == 'september' or month_lower == 'october' or month_lower == 'november':
        return "Autumn"
    elif month_lower == 'december' or month_lower == 'january' or month_lower == 'february':
        return "Winter"
    elif month_lower == 'march' or month_lower == 'april' or month_lower == 'may':
        return "Spring"
    elif month_lower == 'june' or month_lower == 'july' or month_lower == 'august':
        return "Summer"
    else:
        return "Enter a valid month"


print(f"Season: {check_season('APRIL')}")


def calculate_slope(x1, x2, y1, y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope


print(calculate_slope(2, 3, 4, 5))


def solve_quadratic_eqn(a, b, c):
    print(f"Equation: {a}x^2 + {b}x + {c} = 0")
    result_one = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
    result_two = (-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
    return result_one, result_two


print(f"Possible results: {solve_quadratic_eqn(1, -5, 6)}")


def print_list(lst):
    for item in lst:
        print(item)


list_to_print = [1, 3, 4, 56]
print_list(list_to_print)


def reverse_list(list_to_reverse):
    reversed_list = []
    for ele in range(len(list_to_reverse) - 1, -1, -1):
        reversed_list.append(list_to_reverse[ele])
    return reversed_list


print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))


def capitalize_list(list_to_shout):
    capitalized_list = []
    for ele in list_to_shout:
        capitalized_list.append(str(ele).upper())
    return capitalized_list


print(capitalize_list(['january', 'april', 'march']))


def add_item(list_to_add, item_to_add):
    list_to_add.append(item_to_add)
    return list_to_add


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))


def remove_item(list_remove, item_remove):
    list_remove.remove(item_remove)
    return list_remove


print(remove_item(food_staff, 'Mango'))
print(remove_item(numbers, 3))


def sum_of_numbers(range_sum):
    sum_all = 0
    for n in range(range_sum + 1):
        sum_all += n
    return sum_all


print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))


def sum_of_odds(sum_odd):
    sum_all_odds = 0
    for n in range(sum_odd + 1):
        if n % 2 != 0:
            sum_all_odds += n
    return sum_all_odds


print(sum_of_odds(100))


def sum_of_even(sum_even):
    sum_all_even = 0
    for n in range(sum_even + 1):
        if n % 2 == 0:
            sum_all_even += n
    return sum_all_even


print(sum_of_even(100))


def evens_and_odds(count_evens_odds):
    count_evens = 0
    count_odds = 0
    for ite in range(count_evens_odds + 1):
        if ite % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1
    return count_evens, count_odds


print(f"Even: {evens_and_odds(100)[0]} Odd: {evens_and_odds(100)[1]}")


def factorial(num_factorial):
    sum_factorial = 1
    for s in range(1, num_factorial + 1):
        sum_factorial *= s
    return sum_factorial


print(factorial(5))


def is_empty(param_empty):
    if len(param_empty) == 0:
        return 'Empty'
    else:
        return 'Not empty'


empty_list = []
not_empty = 'a'
print(is_empty(empty_list))
print(is_empty(not_empty))


def is_prime(prime):
    prime_number = True
    for p in range(2, prime):
        if prime % p == 0:
            prime_number = False
    return prime_number


check_prime = 31
print(f"{check_prime} is prime: {is_prime(check_prime)}")


def unique_item(unique_list):
    if len(unique_list) == len(set(unique_list)):
        return "All items are unique"
    else:
        return "Not all items are unique"


print(unique_item([1, 2, 3, 4, 5, 6, 6]))


def check_data_type(type_list):
    data_type = type(type_list[0])
    same_type_flag = True
    for t in type_list:
        if data_type != type(t):
            same_type_flag = False
    if same_type_flag:
        return "All items have the same type"
    else:
        return "Not items have the same type"


print(check_data_type([1, 2, 3, 4, 5, 6, 'A']))
