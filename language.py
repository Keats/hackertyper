import os
import random
import re
import sys

def index_project(path):
    file_list = []
    for path, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_list.append(os.path.join(path, file))

    return file_list


def tokens():
    py_files = index_project('django')
    while True:
        filename = random.choice(py_files)
        for token in tokens_from_file(filename):
            yield token


def tokens_from_file(path):
    with open(path) as f:
        return re.findall(
            r'\w+|\s+|'
            "'.*?'"
            '".*?"'
            r'|[^#]|#[^\n]*', f.read())


if __name__ == '__main__':
    for t in tokens():
        sys.stdout.write(t)
