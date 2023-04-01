import json
import re

# Exercise 1
list_of_files = ['../data/obama_speech.txt',
                 '../data/michelle_obama_speech.txt',
                 '../data/donald_speech.txt',
                 '../data/melina_trump_speech.txt']


def count_lines_words(file):
    with open(file) as f:
        lines = f.read().splitlines()
    word_count = sum([len(elements) for elements in lines])
    file_name = file.split('/')[-1]
    print(f"Number of lines in {file_name} is: {len(lines)}")
    print(f"Number of words in {file_name} is: {word_count}")


# for s in list_of_files:
#     count_lines_words(s)

# Exercise 2
def most_spoken_language(json_file, positions):
    with open(json_file, encoding='utf-8') as j:
        json_text = j.read()
    json_dict = json.loads(json_text)
    language_dict = {}
    for d in json_dict:
        for l in d['languages']:
            if str(l) not in language_dict:
                language_dict[l] = 1
            else:
                language_dict[l] += 1
    sorted_dict = dict(sorted(language_dict.items(), key=lambda x: x[1], reverse=True))
    sorted_touple = [(v, k) for k, v in sorted_dict.items()]
    return sorted_touple[:positions]


json_file = '../data/countries_data.json'
#print(most_spoken_language(json_file, 5))


# Exercise 3
def most_populated_countries(json_file, positions):
    with open(json_file, encoding='utf-8') as j:
        json_text = j.read()
    json_dict = json.loads(json_text)
    countries_population = []
    for country in json_dict:
        countries_population.append('country')
        countries_population.append(country['name'])
        countries_population.append('population')
        countries_population.append(country['population'])
    res_dct = []
    for i in range(0, len(countries_population), 4):
        res_dct.append({countries_population[i]: countries_population[i+1], countries_population[i+2]: countries_population[i+3]})
    sorted_dict_list = sorted(res_dct, key=lambda d: d['population'], reverse=True)
    return sorted_dict_list[:positions]


#print(most_populated_countries(json_file, 10))


# Exercise 4
def get_from_email_list(txt_file):
    with open(txt_file) as e:
        txt_lines = e.readlines()
    from_lines = []
    for i in txt_lines:
        if i.startswith('From '):
            from_lines.append(i)
    regex_emails = []
    for m in from_lines:
        regex_emails.append(re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', m))
    return regex_emails


#print(get_from_email_list('../data/email_exchanges_big.txt'))


# Exercise 5 and 6
def find_most_common_words(txt_file, positions):
    with open(txt_file) as w:
        txt_lines = w.readlines()
    flattened_list = []
    for item in txt_lines:
        flattened_list.append(re.findall(r'[\w]+', item))
    every_word = [number for row in flattened_list for number in row]
    set_every_word = set(every_word)
    count_every_word = []
    for word in set_every_word:
        count_every_word.append((every_word.count(word), word))
    sorted_count = sorted(count_every_word, key=lambda d: d[0], reverse=True)
    return sorted_count[:positions]


# print(find_most_common_words('../data/obama_speech.txt', 10))
# print(find_most_common_words('../data/michelle_obama_speech.txt', 10))
# print(find_most_common_words('../data/donald_speech.txt', 10))
# print(find_most_common_words('../data/melina_trump_speech.txt', 10))


# Exercise 7
# Find similar words in both files
def find_common_words_texts(txt_file_one, txt_file_two):
    with open(txt_file_one) as txt_one:
        txt_lines_one = txt_one.readlines()
    with open(txt_file_two) as txt_two:
        txt_lines_two = txt_two.readlines()
    primary_list = []
    comparison_list = []
    for item in txt_lines_one:
        primary_list.append(re.findall(r'[\w]+', item))
    for item in txt_lines_two:
        comparison_list.append(re.findall(r'[\w]+', item))
    primary_words = [number for row in primary_list for number in row]
    comparison_words = [number for row in comparison_list for number in row]
    set_primary_words = set(primary_words)
    set_comparison_words = set(comparison_words)
    similar_words = []
    for word in set_primary_words:
        if word in set_comparison_words:
            similar_words.append(word)
    return similar_words


file_path_one = '../data/michelle_obama_speech.txt'
file_path_two = '../data/melina_trump_speech.txt'
#print(find_common_words_texts(file_path_one, file_path_two))


# Exercise 8
#print(find_most_common_words('../data/romeo_and_juliet.txt', 10))

# Exercise 9
import csv

def count_words_text(file_path):
    python_count = 0
    javascript_count = 0
    java = 0
    regex_python = re.compile(r'.?[Pp]ython.?')
    regex_javascript = re.compile(r'.?[Jj]ava[Ss]cript.?')
    regex_java = re.compile(r'Java[^sS]')
    with open(file_path) as f:
        csv_reader = csv.reader(f, delimiter=',')
        flattened_list = [number for row in csv_reader for number in row]
        for line in flattened_list:
            if regex_python.findall(line):
                python_count += 1
            if regex_javascript.findall(line):
                javascript_count += 1
            if regex_java.findall(line):
                java += 1
        print(f"Python or python: {python_count}")
        print(f"JavaScript: {javascript_count}")
        print(f"Java: {java}")


count_words_text('../data/hacker_news.csv')
