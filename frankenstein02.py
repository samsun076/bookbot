# solution based on more simple functions

def main():
    book = "books/frankenstein.txt"
    frankenstein = get_book_text(book)
    num_words = get_word_count(frankenstein)
    letter_count = get_letter_count(frankenstein)
    print(f"{num_words} words found in {book}")
    print("###")
    print(letter_count)

def get_book_text(book_name):
    with open(book_name) as f:
        return f.read()

def get_word_count(book):
    return len(book.split())

def get_letter_count(book):
    counter = {}
    for letter in book.lower():
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

main()


