
empty_list = []

list_six_items = [1, 2, 3, 4, 5, 6]
print(list_six_items)
print("Number of items: " + str(len(list_six_items)))
print("First item: " + str(list_six_items[0]))
print("Midle item: " + str(list_six_items[int(len(list_six_items)/2)]))
print("First item: " + str(list_six_items[-1]))

mixed_data_types = ['Eric', 38, 1.89, 'Maried', 'New Zealand']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Amazon']
print(it_companies)
print(f"Number of companies: {str(len(it_companies))}")
print("Number of items: " + str(len(list_six_items)))
print("First company: " + str(it_companies[0]))
print("Midle company: " + str(it_companies[int(len(it_companies)/2)]))
print("First company: " + str(it_companies[-1]))

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Xero')
print(it_companies)

it_companies.insert(int(len(it_companies)/2), 'Oracle')
print(it_companies)

item_to_uper = it_companies[1].upper()
it_companies[1] = item_to_uper
print(it_companies)

print('#; '.join(it_companies))

print(f"IBM is in list: {'IBM' in it_companies}")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[-5:])

print(it_companies[0:5])

it_companies.pop(int(len(it_companies)/2))
print(it_companies)

del it_companies[0]
print(it_companies)

del it_companies[int(len(it_companies)/2)]
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, 'SQL')
full_stack.insert(5, 'Python')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(f"Min age: {ages[0]}")
print(f"Max age: {ages[-1]}")

if len(ages) % 2 == 0:
    median = int((ages[int(len(ages)/2)] + ages[int((len(ages)/2)-1)])/2)
    print(f"Median value: {median}")

sum_list = 0
for i in ages:
    sum_list += i
average = sum_list / int(len(ages))
print(f"Average value: {average}")

print(f"Age range: {ages[-1] - ages[0]}")

print(f"Low range: {abs(ages[0] - average):.2}")
print(f"Higher range: {abs(ages[-1] - average):.2}")
