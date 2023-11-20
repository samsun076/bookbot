# solution based on more simple functions
# solution based on sorting letter only in isalpha

def main():
    book = "books/frankenstein.txt"
    frankenstein = get_book_text(book)
    num_words = get_word_count(frankenstein)
    letter_count = get_letter_count(frankenstein)
    
    print(f"--- Begin report of {book} --- ")
    print(f"{num_words} were found in the document \n")
    book_letter = list(letter_count.keys())
    book_letter.sort()
    for letter in book_letter:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")
    print(f"--- End report ---")

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


