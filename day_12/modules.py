from random import random, randint
import string


def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname


def random_user_id():
    user_id = ''
    source = string.ascii_letters + string.digits
    let = 0
    while let < 6:
        user_id += source[randint(0, len(source) - 1)]
        let += 1
    return user_id


def random_user_generate_id():
    number_ids = int(input("Enter the number of IDs to be created: "))
    id_length = int(input("Enter the length of the IDs: "))
    source = string.ascii_letters + string.digits
    for user in range(0, number_ids):
        user_id = ''
        let = 0
        while let < id_length:
            user_id += source[randint(0, len(source) - 1)]
            let += 1
        print(f"User {user + 1} ID: {user_id}")


def rgb_color_gen():
    red = randint(000, 255)
    green = randint(000, 255)
    blue = randint(000, 255)
    return f"rgb({red},{green},{blue})"


def list_of_hexa_colors(num_of_colors=1):
    list_hexa_colors = []
    source = string.digits + 'a' + 'b' + 'c' + 'd' + 'e' + 'f'
    for c in range(0, num_of_colors):
        color = ''
        let = 0
        while let < 6:
            color += source[randint(0, len(source) - 1)]
            let += 1
        list_hexa_colors.append(f"#{color}")
    return list_hexa_colors


def list_of_rgb(num_of_colors):
    list_of_colors = []
    for c in range(0, num_of_colors):
        list_of_colors.append(rgb_color_gen())
    return list_of_colors


def generate_colors(rgb, number_of_colors):
    list_of_colors = []
    for i in range(0, number_of_colors):
        if rgb == 'rgb':
            list_of_colors.append(rgb_color_gen())
        else:
            list_of_colors.append(list_of_hexa_colors())
    return list_of_colors


def shuffle_list(list_of_numbers):
    shuffled_list = []
    for n in range(0, len(list_of_numbers)):
        index = randint(0, len(list_of_numbers) - 1)
        shuffled_list.append(list_of_numbers[index])
        list_of_numbers.pop(index)
    return shuffled_list


def seven_random_numbers():
    random_seven_numbers = []
    source = list(range(1, 10))
    iterator = 0
    for i in range(0, 7):
        index = randint(0, 8 - iterator)
        print(index)
        random_seven_numbers.append(source[index])
        source.pop(index)
        iterator += 1
    return random_seven_numbers

