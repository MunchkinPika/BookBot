##Bookbot main code


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents

from stats import count_words

def main (): 
    #relative path to book 
    path_to_book = 'books/frankenstein.txt'
    text = get_book_text(path_to_book)
    count_words(text)


main ()
