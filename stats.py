def count_words(text):  
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
    
def count_characters(text):
    text = text.lower()
    char_freq = {}
    
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq