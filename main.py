##Bookbot main code

import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    print("============ BOOKBOT ============")
    text = get_book_text(path_to_book)
    print(f"Analyzing book found at {path_to_book}...")

    # Count and print number of words
    num_words = count_words(text)

    # Count characters
    character_frequencies = count_characters(text)
    sorted_characters = sort_characters(character_frequencies)

    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============== END ===================")

main()