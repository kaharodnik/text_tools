def count_words(filename):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
        words = contents.split()
        num_words = len(words)
        num_types = len(set(words))
        print(f"the file {filename} has about {num_words} words and {num_types} unique words.")
                
filename = 'shakespeare-hamlet.txt'
count_words(filename)
