
thirty = "Thirty "
days = "Days "
of = "Of "
python = "Python"
print(thirty + days + of + python)

coding = "Coding "
for_s = "For "
all = "All"
print(coding + for_s + all)

company = coding + for_s + all
print(company)
print(f"company length: {len(company)}")
print(company.upper())
print(company.lower())
print(f"Capitalize: {company.capitalize()}")
print(f"Title: {company.title()}")
print(f"Swapcase: {company.swapcase()}")

print(f"Slice first letter: {company[1:len(company)]}")
print(f"Find Coding Index: {company.find('Coding')}")

print(f"Replace: {company.replace('Coding', 'Python')}")

string_two = "Python For Everyone"
print(f"Replace 2: {string_two.replace('Everyone', 'All')}")

print(f"Split: {company.split()}")

string_three = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(f"Split coma: {string_three.split(',')}")

print(f"String index 0: {company[0]}")

print(f"Last index: {company.rindex(company[-1])}")

print(f"Index 10: '{company[10]}'")

splited = string_two.split()
print(splited[0][0] + splited[1][0] + splited[2][0])

split_string = company.split()
print(split_string[0][0] + split_string[1][0] + split_string[2][0])

print(f"C index: {company.index('C')}")
print(f"F index: {company.index('F')}")

string_four = "Coding For All People"
print(f"l index: {string_four.rindex('l')}")

sentence_one = 'You cannot end a sentence with because because because is a conjunction'
print(f"Index because: {sentence_one.index('because')}")
print(f"Last because index: {sentence_one.rindex('because')}")

sub_string_one = sentence_one.split(' because because because ')
print(f"Split because: {sub_string_one[0]} {sub_string_one[1]}")

print(f"Startswith: {company.startswith('Coding')}")
print(f"Startswith: {company.endswith('Coding')}")

print(f"Remove space: '{'   Coding For All      '.replace(' ','')}'")

print(f"Is identifier: {'30DaysOfPython'.isidentifier()}")
print(f"Is identifier: {'thirty_days_of_python'.isidentifier()}")

python_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libs))

string_five = """I am enjoying this challenge.
I just wonder what is next."""
print(string_five.split('\n'))

headers = ['Name\t', 'Age', 'Country', 'City']
person_one = ['Asabeneh', '250', 'Finland', 'Helsinki']
print('\t '.join(headers))
print('\t '.join(person_one))

radius = 10
area = 3.14 * radius ** 2
print(f"radius = {radius}")
print("area = 3.14 * radius ** 2")
print(f"The area of the circle with radius {radius} is {area} meters square.")

num_one = 8
num_two = 6
print(f"{num_one} + {num_two} = {num_one + num_two}")
print(f"{num_one} - {num_two} = {num_one - num_two}")
print(f"{num_one} * {num_two} = {num_one * num_two}")
print(f"{num_one} / {num_two} = {(num_one / num_two):.2f}")
print(f"{num_one} % {num_two} = {num_one % num_two}")
print(f"{num_one} // {num_two} = {num_one // num_two}")
print(f"{num_one} ** {num_two} = {num_one ** num_two}")
