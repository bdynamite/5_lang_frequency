import re
import collections


def load_data(filepath):
    try:
        with open(filepath, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        print("file not found!")
        exit()


def get_most_frequent_words(words, n):
    words_counter = collections.Counter(words)
    return words_counter.most_common(n)


def get_words(text):
    templ = re.compile(r'\w+')
    return templ.findall(text)


if __name__ == '__main__':
    data = load_data(input('input text path: '))
    words = get_words(data)
    most_frequent = get_most_frequent_words(words, 10)
    print(most_frequent)