# solution based on more simple functions
# solution based on sorting letter only in isalpha

def main():
    book = "books/frankenstein.txt"
    frankenstein = get_book_text(book)
    num_words = get_word_count(frankenstein)
    letter_count = get_letter_count(frankenstein)
    sorted_letter_count = letter_count_to_sorted_list(letter_count)

    print(f"--- Begin report of {book} --- ")
    print(f"{num_words} were found in the document \n")
    
    
    for x in sorted_letter_count:
        if x["char"].isalpha():
            print(f"The {x['char']} character was found {x['num']}")
       
    
    print(f"--- End report ---")


def sort_on(d):
    return d["num"]

def letter_count_to_sorted_list(letter_count_dict):
    sorted_list = []
    for ch in letter_count_dict:
        sorted_list.append({"char":ch, "num":letter_count_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


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


