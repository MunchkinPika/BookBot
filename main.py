##Bookbot main code


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words
from stats import count_characters

def main (): 
    #relative path to book 
    path_to_book = 'books/frankenstein.txt'
    text = get_book_text(path_to_book) 

  # Count and print number of words
    count_words(text)
    
    # Count characters
    character_frequencies = count_characters(text)
    
    for i, (char, count) in enumerate(character_frequencies.items()):
        print(f"'{char}': {count}")

main ()
