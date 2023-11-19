# solution based on more simple functions

def main():
    book = "books/frankenstein.txt"
    frankenstein = get_book_text(book)
    num_words = get_word_count(frankenstein)
    print(f"{num_words} words found in {book}")

def get_book_text(book_name):
    with open(book_name) as f:
        return f.read()

def get_word_count(book):
    return len(book.split())

main()


