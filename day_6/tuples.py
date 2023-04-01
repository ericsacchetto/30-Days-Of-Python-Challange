
empty_tuple = ()

brothers = ('Sherlock', 'Conan', 'Poirot')
print(brothers)
sisters = ('Agatha', 'Marple', 'Debbie')
print(sisters)

siblings = brothers + sisters
print(siblings)

print(f"Number of siblings: {len(siblings)}")

parents = ('Jose', 'Celia')
family_members = parents + siblings
print(f"Whole family: {family_members}")

parent_one, parent_two, *rest = family_members
parent_new = parent_one, parent_two
print(f"Unpacked parents: {parent_new}")
siblings_new = rest
print(f"Unpacked siblings: {siblings_new}")

fruits = ('Peach', 'Lemon')
vegetables = ('Brocoli', 'carrot')
animal = ('chicken', 'fish')
food_stuff_tp = fruits + vegetables + animal
print(food_stuff_tp)
print(f"Middle item(s): {food_stuff_tp[2:4]}")

print(f"First three items: {food_stuff_tp[:3]}")
print(f"Last three items: {food_stuff_tp[-3:]}")

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print(f"Is Estonia in Nordic Countries: {'Estonia' in nordic_countries}")
print(f"Is Iceland in Nordic Countries: {'Iceland' in nordic_countries}")

