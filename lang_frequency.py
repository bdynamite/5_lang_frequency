import re
import collections


def load_data(filepath):
    try:
        with open(filepath, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        print("file not found!")
        return None


def get_most_frequent_words(words, words_quantity):
    words_counter = collections.Counter(words)
    return words_counter.most_common(words_quantity)


def get_words(text):
    templ = re.compile(r'\w+')
    return templ.findall(text)


def print_words(words_with_counter):
    print('\n'.join(['word "{}" occures {} times'.format(x[0], x[1]) for x in words_with_counter]))


if __name__ == '__main__':
    text = load_data(input('input text path: '))
    if text:
        words_quantity = int(input('how many words do you want to see? '))
        words = get_words(text)
        most_frequent = get_most_frequent_words(words, words_quantity)
        print_words(most_frequent)