filename = 'shakespeare-hamlet.txt'
with open(filename, encoding='utf-8') as f:
    contents = f.read()
    words = contents.split()
    num_words = len(words)
    print(f"the file {filename} has about {num_words} words.")

