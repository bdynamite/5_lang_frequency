import chardet
import os

SYMBOLS = ['.', ',', '!', '?']


def load_data(text_path):
    encoding = get_encoding(text_path)
    with open(text_path, 'r', encoding=encoding) as file:
        lines = file.readlines()
        return ' '.join(lines)


def get_encoding(path_to_file_text):
    with open(path_to_file_text, 'rb') as source:
        lines = source.read()
        result = chardet.detect(lines)
        if result['encoding'] is None:
            raise Exception("Unknown encoding!")
        else:
            return result['encoding']


def get_most_frequent_words(text):
    dict_of_words = make_dict(words)
    sorted_items = sorted(dict_of_words.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        print('{}) {}'.format(i + 1, sorted_items[i]))


def make_dict(list_of_words):
    dict_of_words = {}
    for element in list_of_words:
        if element in dict_of_words:
            dict_of_words[element] += 1
        else:
            dict_of_words[element] = 1
    return dict_of_words


def delete_symbol(text, symbol):
    return text.replace(symbol, '')


def get_words(text):
    for element in SYMBOLS:
        text = delete_symbol(text, element)
    return text.split()


if __name__ == '__main__':
    my_text = input('input text path: ')
    print(os.path.exists(my_text))
    string = load_data(my_text)
    words = get_words(string)
    get_most_frequent_words(words)
