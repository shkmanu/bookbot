def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        count = len(words)
        print(count)

word_count()