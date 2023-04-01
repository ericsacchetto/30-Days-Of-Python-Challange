dog = {}

dog['name'] = 'Archie'
dog['color'] = 'Caramelo'
dog['breed'] = 'Mix'
dog['legs'] = 5
dog['age'] = 10

print(dog)

student = {'first_name': 'Derek', 'last_name': 'Dominos', 'gender': 'Male', 'age': 45, 'marital status': 'Unknown',
           'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'], 'country': 'USA', 'city': 'Denver', 'address': 'Redacted'}
print(student)
print(f"Student dictionary length: {len(student)}")

skill_value = student.values()
print(f"Student skill: {student['skills']} ({type(student['skills'])})")
student['skills'].append('Oracle')
student['skills'].append('Embedded')

print(f"Improved skills: {student['skills']}")

print(f"Student keys: {student.keys()}")
print(f"Student keys: {student.values()}")

print(student.items())

del student['last_name']
print(f"Student wihtout last name: {student}")

del dog



