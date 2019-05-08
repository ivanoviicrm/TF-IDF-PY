import nltk
from config import config
from utils import utils
import os
import math


def calculate_tf(text):
    tokens = nltk.word_tokenize(text, "spanish")

    # Cuento cuantas veces se repite cada palabra (una a una)
    tf_dictionary = {}
    for word in tokens:
        if word in tf_dictionary:
            tf_dictionary[word] += 1
        else:
            tf_dictionary[word] = 1

    # Hago el calculo del TF
    for word in tf_dictionary:
        tf_dictionary[word] = tf_dictionary[word] / len(tokens)

    return tf_dictionary


def calculate_occurrences(tf_dictionary={}, count_dictionary={}):

    for token in tf_dictionary:
        if token in count_dictionary:
            count_dictionary[token] += 1
        else:
            count_dictionary[token] = 1

    return count_dictionary


def calculate_idf(count_dictionary={}, num_files=1):
    idf_dictionary = {}

    for word in count_dictionary:
        idf_dictionary[word] = math.log(num_files / count_dictionary[word])

    return idf_dictionary


count_dictionary = {}
txt_files = utils.get_files_in_path(config.DEFAULT_TXT_PATH, extension="txt")
for file in txt_files:
    text = utils.read_txt(os.path.join(config.DEFAULT_TXT_PATH, file))
    tf_dictionary = calculate_tf(text)
    count_dictionary = calculate_occurrences(tf_dictionary, count_dictionary)

print(calculate_idf(count_dictionary, len(txt_files)))
