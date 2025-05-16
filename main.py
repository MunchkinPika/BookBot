##Bookbot main code


def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
        return file_contents
def count_words(text):  
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")

def main (): 
    #relative path to book 
    path_to_book = 'books/frankenstein.txt'
    text = get_book_text(path_to_book)
    count_words(text)


main ()
