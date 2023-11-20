# initial solution with just one function
# 02 file breaking the function into 2 more simple functions

def word_count(source_file):
    with open(source_file) as file:
        contents = file.read()
    return len(contents.split())




frankenstein = "books/frankenstein.txt"
print(word_count(frankenstein))
