#counting number of words for files with .txt in a directory
import os

def count_words(filename):
    with open(filename, 'r') as f:
        contents = f.readlines()
        words = contents.split()
        num_words = len(words)
        num_types = len(set(words))
        print(f"the file {filename} has about {num_words} words and {num_types} unique words.")


dir = 'C:\\Users\\Katya\\Desktop\\text\\gutenberg'
for f in os.listdir(dir):
    if f.endswith('.txt'):
        print(f)
        count_words(f)

