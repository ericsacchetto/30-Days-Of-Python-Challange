from data import countries as county_list

count = 0
print("Iterating to 10 using While")
while count <= 10:
    print(count)
    count += 1

print("Iterating to 10 using For")
for iterator in range(11):
    print(iterator)

print("Reverse iterating using While")
count_reverse = 10
while count_reverse >= 0:
    print(count_reverse)
    count_reverse -= 1

print("Reverse iterating using For")
for iterator_reverse in range(10, -1, -1):
    print(iterator_reverse)

for ite in range(8):
    print("#" * ite)

for x in range(9):
    print("# " * 8)

for number in range(11):
    print(f"{number} * {number} = {number * number}")

lib_items = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in lib_items:
    print(i)

for h in range(101):
    if (h % 2) == 0:
        print(h)

for h in range(101):
    if (h % 2) != 0:
        print(h)

print("Level 2 exercises")

sum = 0
for j in range(101):
    sum += j
print(sum)

sum_eve = 0
sum_odd = 0
for k in range(101):
    if (k % 2) == 0:
        sum_eve += k
    else:
        sum_odd += k
print(f"Odd sum = {sum_odd} and Even sum = {sum_eve}")

print("Leve 3 exercises")

for u in county_list.countries:
    if 'land' in u:
        print(u)

fruit_list = ['banana', 'orange', 'mango', 'lemon']
itera = len(fruit_list) - 1
for t in fruit_list:
    print(fruit_list[itera])
    itera -= 1

