
# Day 2: 30 Days of python programming
first_name = "Eric"
last_mame = "Sacchetto"
full_mame = last_mame + ", " + first_name
country = "Brasil"
citty = "Sao Paulo"
age = 39
year = 2023
is_married = True
is_true = False
is_light_on = False
fruit, is_light_on, salad = "", "", ""


print(f"{first_name} type: {type(first_name)}")
print(f"{last_mame} type: {type(last_mame)}")
print(f"{full_mame} type: {type(full_mame)}")
print(f"{country} type: {type(country)}")
print(f"{citty} type: {type(citty)}")
print(f"{age} type: {type(age)}")
print(f"{year} type: {type(year)}")
print(f"{is_married} type: {type(is_married)}")
print(f"{is_true} type: {type(is_true)}")
print(f"{is_light_on} is_light_on: {type(is_light_on)}")
print(f"{first_name} type: {type(first_name)}")

print(f"Lenght of my first name: {len(first_name)}")
print(f"First name size: {len(first_name)} last name size: {len(last_mame)}")

num_one = 5
num_two = 4

total = num_one + num_two
dif = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.14 * radius**2
print(f"Area of circle: {area_of_circle}")
circum_of_circle = 2 * 3.14 * radius
print(f"Circunference of circle: {circum_of_circle}")

user_radius = input("Radius of circle: ")
print(f"Area calculated: {3.14 * int(user_radius)**2}")

first_name = input("Type your first name: ")
last_mame = input("Type your last name: ")
country = input("Type your country: ")
age = input("Type your age: ")
