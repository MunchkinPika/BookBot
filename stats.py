def count_words(text):  
    words = text.split()
    num_words = len(words)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
def count_characters(text):
    text = text.lower()
    char_freq = {}
    
    for char in text:
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    

    return char_freq

def sort_characters(char_dict):
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    
    # Sort the list in-place by "num", descending
    char_list.sort(key=lambda x: x["num"], reverse=True)
    
    return char_list