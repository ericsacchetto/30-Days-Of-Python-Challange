
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_list = [i for i in numbers if i <= 0]
print(filtered_list)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [number for row in list_of_lists for number in row]
flattened_list_two = [number for row in flattened_list for number in row]
print(flattened_list_two)

list_of_tuples = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
for i in list_of_tuples:
    print(i)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [list(country) for row in countries for country in row]
for i in flattened_countries:
    i.insert(1, i[0][0:3])
    i[0] = i[0].upper()
    i[1] = i[1].upper()
    i[2] = i[2].upper()
print(flattened_countries)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

flattened_list = [list(country) for row in countries for country in row]
list_output = []
dict_output = {}
for k in flattened_list:
    dict_output['country'] = k[0].upper()
    dict_output['city'] = k[1].upper()
    list_output.append(dict_output.copy())

print(list_output)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flattened_names = [list(name) for row in names for name in row]
name_output = []
for n in flattened_names:
    name_output.append(f"{n[0]} {n[1]}")

print(name_output)
