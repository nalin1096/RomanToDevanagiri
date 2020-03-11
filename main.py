import sys
from utils.transliterate import *

def prepare_data (data_file):
    data_lines = []
    with open(data_file) as f:
        for line in f:
            if (line != '\n'):
                data_lines.append(line.lower())
    return data_lines


if __name__ == "__main__":
    try:
        data_file = sys.argv[1]
        data_lines = prepare_data(data_file)
        for line in data_lines:
            print(transliterate(line))
    except:
        data = input("Enter text to be transliterated: ")
        output = transliterate(data)
        print(output)
