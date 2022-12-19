#counting number of words for files with .txt in a directory
import os
'''Count the number of tokens and types in a file'''

def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except UnicodeDecodeError:
        print(f"Sorry, cannot process {filename}")
    except FileNotFoundError:
        print(f"Sorry, cannot find {filename}")
    else:
        words = contents.split()
        num_words = len(words)
        num_types = len(set(words))
        print(f"the file {filename} has about {num_words} words and {num_types} unique words.")


dir = 'C://Users//Katya//Desktop//text//gutenberg'
os.chdir(dir)
for file in os.listdir(dir):
    if file.endswith(".txt"):
        print(file)
        count_words(file)

