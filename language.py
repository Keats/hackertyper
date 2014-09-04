import os
import random
import re
import sys
from collections import defaultdict, Counter

def index_project(path):
    file_list = []
    for path, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_list.append(os.path.join(path, file))

    return file_list


def tokens():
    model = create_markov_model()
    tok = None
    while True:
        choices = model[tok]
        if not choices:
            tok = None
            continue
        nexttok = random.choice(choices)
        if nexttok == tok:
            tok = None
            continue
        tok = nexttok
        yield tok


def tokens_from_file(path):
    with open(path) as f:
        return f.readlines()
        return re.findall(
            r'\w+|\s+|'
            "'.*?'"
            '".*?"'
            r'|[^#]|#[^\n]*', f.read())


def create_markov_model():
    py_files = index_project('django')
    bigrams = defaultdict(list)
    for file in py_files:
        tokens = tokens_from_file(file)
        for word1, word2 in zip([None] + tokens, tokens):
            bigrams[word1].append(word2)
    return bigrams


if __name__ == '__main__':
    for t in tokens():
        sys.stdout.write(t)
#    print create_markov_model()
