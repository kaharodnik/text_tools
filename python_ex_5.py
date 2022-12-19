#counting number of words for files with .txt in a directory
import os

def count_words(filename):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        words = contents.split()
        num_words = len(words)
        num_types = len(set(words))
        print(f"the file {filename} has about {num_words} words and {num_types} unique words.")


dir = './gutenberg'
for file in os.listdir(dir):
    if file.endswith(".txt"):
        print(file)
        count_words(file)

