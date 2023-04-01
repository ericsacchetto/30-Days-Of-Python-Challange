import re
import requests
import numpy


# Exercise 1
def find_most_common_words_url(url, positions):
    flattened_list = [re.findall(r'[\w]+', url)]
    every_word = [number for row in flattened_list for number in row]
    set_every_word = set(every_word)
    count_every_word = []
    for word in set_every_word:
        count_every_word.append((every_word.count(word), word))
    sorted_count = sorted(count_every_word, key=lambda d: d[0], reverse=True)
    return sorted_count[:positions]


url = 'http://www.gutenberg.org/files/1112/1112.txt'
# response = requests.get(url)
# print(find_most_common_words_url(response.text, 10))


# Exercise 2
def read_api_text(api_url):
    response_url = requests.get(api_url)
    return response_url.json()


def get_cats_weight(cats_json_arg):
    regex_weight = re.compile(r'\d+')
    cats_weight = []
    for i in cats_json_arg:
        cats_weight.append(re.findall(regex_weight, i['weight']['metric']))
    return [int(number) for row in cats_weight for number in row]


def print_cats_weight_data(weight_list):
    min_weight = min(weight_list)
    print(f"Cats minimum weight: {min_weight}")
    max_weight = max(weight_list)
    print(f"Cats maximum weight: {max_weight}")
    mean_weight = numpy.mean(weight_list)
    print(f"Cats mean weight: {mean_weight:.2f}")
    median_weight = numpy.median(weight_list)
    print(f"Cats median weight: {median_weight}")
    std_weight = numpy.std(weight_list)
    print(f"Cats deviation weight: {std_weight:.2f}")


# cats_api = 'https://api.thecatapi.com/v1/breeds'
# cats_json = read_api_text(cats_api)
# cats_weight_list = get_cats_weight(cats_json)
# print_cats_weight_data(cats_weight_list)


def get_cats_lifespan(cats_json_lifespan):
    regex_lifespan = re.compile(r'\d+')
    cats_lifespan = []
    for i in cats_json_lifespan:
        cats_lifespan.append(re.findall(regex_lifespan, i['life_span']))
    return [int(number) for row in cats_lifespan for number in row]


def print_cats_lifespan_data(lifespan_list):
    min_lifespan = min(lifespan_list)
    print(f"Cats minimum lifespan: {min_lifespan}")
    max_lifespan = max(lifespan_list)
    print(f"Cats maximum lifespan: {max_lifespan}")
    mean_lifespan = numpy.mean(lifespan_list)
    print(f"Cats mean lifespan: {mean_lifespan:.2f}")
    median_lifespan = numpy.median(lifespan_list)
    print(f"Cats median lifespan: {median_lifespan}")
    std_lifespan = numpy.std(lifespan_list)
    print(f"Cats deviation lifespan: {std_lifespan:.2f}")


# lifespan_cats_list = get_cats_lifespan(cats_json)
# print_cats_lifespan_data(lifespan_cats_list)


def get_cats_breed_country(cats_json_breed):
    cats_country = []
    for i in cats_json_breed:
        cats_country.append(i['origin'])
    set_cats_country = set(cats_country)
    print("Country and number of breeds:")
    for n in sorted(set_cats_country):
        count = 0
        for m in cats_json_breed:
            if n == m['origin']:
                count += 1
        print(f"{n} {count}")


# get_cats_breed_country(cats_json)


# Exercise 3
# country_area_url = 'https://restcountries.com/v3.1/all?fields=name,area'
# country_area_list = read_api_text(country_area_url)


def print_country_area(country_area_json):
    country_list = []
    for i in country_area_json:
        country_list.append([i['name']['official'], i['area']])
    sorted_list = sorted(country_list, key=lambda x: x[1], reverse=True)
    for c in sorted_list[:10]:
        print(c)


# print_country_area(country_area_list)


country_languages_url = 'https://restcountries.com/v3.1/all?fields=languages'
country_languages_list = read_api_text(country_languages_url)


def print_country_languages(languages_json):
    language_list = []
    for i in languages_json:
        language_list.append(i['languages'])
    list_of_languages = []
    for j in language_list:
        list_of_languages.append(list(j.values()))
    flattened_list = [row for column in list_of_languages for row in column]
    set_flat_list = set(flattened_list)
    result_list = []
    for l in set_flat_list:
        result_list.append([l, flattened_list.count(l)])
    sorted_list = sorted(result_list, key=lambda x: x[1], reverse=True)
    for s in sorted_list[:10]:
        print(s)
    print(f"Total number of languages: {len(flattened_list)}")
    print(f"Total number of unique languages: {len(set_flat_list)}")


print_country_languages(country_languages_list)

