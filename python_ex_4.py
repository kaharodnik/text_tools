#!/bin/bash

import os


def count_words(filename):
                with open(filename, encoding='utf-8') as f:
                    contents = f.read()
                    words = contents.split()
                    num_words = len(words)
                    num_types = len(set(words))
                    print(f"the file {filename} has {num_words} words and {num_types} unique words.")
                    
filenames = ['shakespeare-hamlet.txt', 'shakespeare-macbeth.txt']

for filename in filenames:
    count_words(filename)
