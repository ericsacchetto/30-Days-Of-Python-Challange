try:
    print('Trying to calculate 1 + A')
    results = 1 + 'A'
except Exception as e:
    print(f'Something went wrong and this is why: {e}')
else:
    print(results)
finally:
    print("Thank you")


# Unpacking

def sum_of_few_numbers(num1, num2, num3):
    return num1 + num2 + num3

lst1 = [1, 2, 3]
print(sum_of_few_numbers(*lst1))

range_args = (0, 7)     # work with [0, 7] as well
numbers = range(*range_args)
print(list(numbers))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
FN, SW, *others, IC = countries
print(FN, IC, SW, others)


def unpacking_person_info(**kwargs):
    return f'{kwargs["name"]} {kwargs["surname"]} lives in {kwargs["city"]}, {kwargs["country"]}. ' \
           f'He is {kwargs["age"]} years old.'

dct = {
    'name': 'Shaun',
    'surname': 'The Sheep',
    'country': 'New Zealand',
    'city': 'Hamilton',
    'age': 25
}
print(unpacking_person_info(**dct))


# Enumerate

for index, item in enumerate(countries):
    print(index, item)
    if index == 4:
        print(f"This is the last index {index}")


# Zip

first_name = ['Eric', 'Vanessa', 'Shaun']
last_name = ['Sacchetto', 'Da Silva', 'The Sheep']
first_and_last_name = []
for f, l in zip(first_name, last_name):
    first_and_last_name.append({'first name': f, 'last name': l})

print(first_and_last_name)


names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names

print(nordic_countries, es, ru)
