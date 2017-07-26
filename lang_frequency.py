import re
import collections

WORDS_QANTITY = 10


def load_data(filepath):
    try:
        with open(filepath, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        print("file not found!")
        exit()


def get_most_frequent_words(words):
    words_counter = collections.Counter(words)
    return words_counter.most_common(WORDS_QANTITY)


def get_words(text):
    templ = re.compile(r'\w+')
    return templ.findall(text)


if __name__ == '__main__':
    text = load_data(input('input text path: '))
    words = get_words(text)
    most_frequent = get_most_frequent_words(words)
    print(most_frequent)