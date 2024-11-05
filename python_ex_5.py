#!/bin/usr/env python3

#counting number of words for files with .txt in a directory
import os

def count_words(filename):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        words = contents.split()
        num_words = len(words)
        num_types = len(set(words))
        print(f"the file {filename} has about {num_words} words and {num_types} unique words.")


dir = "C://Users//Katya//Desktop//Teaching_Fall_2022//TextTools_Fall_22_KA//python_ex//gutenberg"
os.chdir(dir)
for f in os.listdir(dir):
    if f.endswith(".txt"):
        print(f)
        count_words(f)

