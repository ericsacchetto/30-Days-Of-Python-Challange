
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(f"Length if it_companies: {len(it_companies)}")

it_companies.add('Twitter')
print(it_companies)

more_it_companies = ('Adafruit', 'Sparkfun', 'Logitech')
it_companies.update(more_it_companies)
print(it_companies)

print(f"Removing a random company: {it_companies.pop()}")

# it_companies.remove('Sun') # Raises an error because Sun does not exist in it_companies
it_companies.discard('Sun')
print('Discard does not raises and error if item is not found.')

C = A.union(B)
print(C)
# Update puts one into another

print(f"Intersection: {A.intersection(B)}")

print(f"A is subset of B: {A.issubset(B)}")

print(f"Are A and B disjoint: {A.isdisjoint(B)}")

D = A.union(B)
E = B.union(A)
print(f"A union B: {D}")
print(f"B union A: {E}")

print(f"Symmetric difference: {A.symmetric_difference(B)}")

del A
del B

print(f"Age list length: {len(age)}")

age_set = set(age)
print(f"Age set length: {len(age_set)}")

print("Strings is a collection of characters")
print("""Lists are:
- Indexed
- Allow repeated items
- Multiple data types""")
print("""Tuples are:
- Immutables
- Indexed
- Multiple data types""")
print("""Sets are:
- Ordered
- Not indexed
- Multiple data types""")

sentence = "I am a teacher and I love to inspire and teach people"
print(sentence)
sentence_no_space = sentence.replace(' ', '')
sentence_set = set(sentence_no_space)
print(f"Number of unique letters in the sentence: {len(sentence_set)}")

sentence_words = sentence.split(' ')
sentence_words_set = set(sentence_words)
print(f"Number of unique words in the sentence: {len(sentence_words_set)}")
