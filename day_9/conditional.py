#
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are old enough to drive")
# else:
#     print(f"You need to wait {18 - age} years to drive")
#
# my_age = int(input("Enter your age: "))
# friend_age = int(input("Enter your friends age: "))
# age_difference = my_age - friend_age
# if my_age == friend_age:
#     print("You have the same age as your friend!")
# elif age_difference == 1:
#     print("You are one year older than your friend.")
# elif age_difference > 1:
#     print(f"You are {age_difference} years older than your friend.")
# elif age_difference == -1:
#     print("Your friend is one year older than you.")
# elif age_difference < -1:
#     print(f"Your friend is {abs(age_difference)} years older than you.")
#
# number_a = int(input("Enter number A: "))
# number_b = int(input("Enter number B: "))
# result = number_a - number_b
# if result == 0:
#     print("Number A is equal number B.")
# elif result > 1:
#     print("Number A is greater than B")
# else:
#     print("Number B is greater than A")
#
# student_score = int(input("Enter student score: "))
# if student_score <= 49:
#     print("Student grade: F")
# elif 50 <= student_score <= 59:
#     print("Student grade: D")
# elif 60 <= student_score <= 69:
#     print("Student grade: C")
# elif 70 <= student_score <= 79:
#     print("Student grade: B")
# elif 80 <= student_score <= 100:
#     print("Student grade: A")
#
# month = input("Enter your current month: ").lower()
# if month == 'september' or month == 'october' or month == 'november':
#     print("Season is Autumn")
# elif month == 'december' or month == 'january' or month == 'february':
#     print("Season is Winter")
# elif month == 'march' or month == 'april' or month == 'may':
#     print("Season is Spring")
# elif month == 'june' or month == 'july' or month == 'august':
#     print("Season is Summer")
# else:
#     print("Enter a valid month")
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# new_fruit = input("Enter a fruit: ").lower()
# if new_fruit in fruits:
#     print("This fruit already exist in the list")
# else:
#     fruits.append(new_fruit)
#     print(f"New fruit added to the list: {fruits}")

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    middle_item = int(len(person['skills'])/2)
    print(f"Middle skill item: {person['skills'][middle_item]}")

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python was found in skills!")
    else:
        print("Python was not found in skills.")

if 'JavaScript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print("He is a front end developer")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
    print("He is a backend developer")
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
    print("He is a fullstack developer")
else:
    print("unknown title")

if person['is_marred'] and person['country'] == 'Finland':
    print(f"Name: \t\t{person['last_name']}, {person['first_name']}")
    print(f"Age: \t\t{person['age']}")
    print(f"Country: \t{person['country']}")
    print(f"Zipcode: \t{person['address']['zipcode']}")
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
