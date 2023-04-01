from math import sqrt

age = 39
height = 1.89
complex_num = 0 + 0j

print("Triangle area")
base = int(input("Enter triangle base: "))
altura = int(input("Enter triangle height: "))
print(f"Triangle area: {0.5 * altura * base}")

print("Triangle perimeter")
side_a = int(input("Enter triangle side A: "))
side_b = int(input("Enter triangle side B: "))
side_c = int(input("Enter triangle side C: "))
print(f"Triangle perimeter: {side_a + side_b + side_c}")

print("Rectangle area and perimeter")
rect_len = int(input("Enter rectangle length: "))
rect_wid = int(input("Enter rectangle width: "))
print(f"Rectangle area: {rect_wid * rect_len}")
print(f"Rectangle perimeter: {2 * (rect_wid + rect_len)}")

print("Circle area and circumference")
circle_radius = float(input("Enter circle radius: "))
print(f"Circle area: {3.14 * circle_radius**2}")
print(f"Circle circumference: {2 * 3.14 * circle_radius}")

print("Slope")
p1 = [0, -2]
p2 = [1, 0]
slope = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
print(f"Slope: {slope}")

print("Slope and Euclidean distance")
p3 = [2, 2]
p4 = [6, 10]
slope_2 = ((p4[1] - p3[1]) / (p4[0] - p3[0]))
euc_dist = sqrt((p4[1] - p3[1])**2 + (p4[0] - p3[0])**2)
print(f"Slope 2: {slope_2}")
print(f"Euclidean distance: {euc_dist}")

print(f"Comparison slope 1 and slope 2: {slope == slope_2}")

print("Calculating y value")
x = -3
y = x**2 + 6 * x + 9
print(y)

print("Comparing python and dragon")
string_1 = "python"
string_2 = "dragon"
print(f"Comparison: {len(string_1) != len(string_2)}")

print(f"On is in both: {'on' in string_1 and 'on' in string_2}")

print(f"Jargon in: {'jargon' in 'I hope this course is not full of jargon'}")

print(f"No on on dragon and python: {'on' not in string_1 and 'on' not in string_2}")

print(f"Python length: {str(float(len(string_1)))}")

print("Even or odd numbers")
int_list = [1, 2, 3, 4]
for i in int_list:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print(f"Checking 7 // 3 is equal to int 2.7: {(7 // 3 == int(2.7))}")

print(f"Checking type '10' equals type 10: {type('10') == type(10)}")

print(f"Check if int 9.8 equals 10: {int(9.8) == 10}")

print("Calculating salary")
hours_worked = float(input("Enter hours worked: "))
rate_hour = float(input("Enter your rate per hour: "))
print(f"Your weekly earning is: {hours_worked * rate_hour}")

print("Calculate the number of seconds lived")
age_old = int(input("Enter your age: "))
print(f"You have lived {age_old * 365 * 24 * 60 * 60}")

list_num = [0, 1, 0, 1, 1]
for i in range(0, 5):
    list_num[0] += 1
    list_num[1] = 1
    list_num[2] += 1
    list_num[3] = (i+1)**2
    list_num[4] = list_num[3] * (i+1)
    print(f"{list_num[0]} {list_num[1]} {list_num[2]} {list_num[3]} {list_num[4]}")
