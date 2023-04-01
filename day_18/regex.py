import re

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love ' \
            'something which can give you all the capabilities to develop an application what else can you love. '

regex_pattern = r'\w+'
match = re.findall(regex_pattern, paragraph)
set_match = set(match)
final_list = []
for e in set_match:
    final_list.append((match.count(e), e))
print(sorted(final_list, reverse=True))


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, " \
       "0 at origin, 4 and 8 in the positive direction. "

regex_pattern2 = r'.\d+'
points = re.findall(regex_pattern2, text)
bigger_distance = (int(points[-1])) - int(points[0])
print(bigger_distance)


variable_one = 'first_name'
variable_two = 'first-name'
variable_three = '1first_name'
variable_four = 'firstname'

regex_pattern3 = r'^\D[^.-]+'
filtered_result_one = re.match(regex_pattern3, variable_one, re.I)
filtered_result_two = re.match(regex_pattern3, variable_two, re.I)
filtered_result_three = re.match(regex_pattern3, variable_three, re.I)
filtered_result_four = re.match(regex_pattern3, variable_four, re.I)

print(f'Valid variables: {filtered_result_one}')
print(f'Valid variables: {filtered_result_two}')
print(f'Valid variables: {filtered_result_three}')
print(f'Valid variables: {filtered_result_four}')


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as 
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s 
mo@tivate yo@u to be a tea@cher!? '''

def remove_symbols(raw_text):
    regex_one = r'%|[$]|@|&|#|;|!'
    clean_text = re.sub(regex_one, '', raw_text)
    return clean_text

def unpack_each_word(text):
    regex_two = r'\w+'
    each_word = re.findall(regex_two, text)
    set_each_word = set(each_word)
    return set_each_word

def count_each_word():
    cleaned_text = remove_symbols(sentence)
    split_words = unpack_each_word(cleaned_text)
    count_words = []
    for w in split_words:
        print(w)
        count_words.append((cleaned_text.count(f'{w} '), w))
    print(count_words)
    sorted_count_sequence = sorted(count_words, reverse=True)
    return sorted_count_sequence[0:3]

print(count_each_word())
