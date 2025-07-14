def get_num_words(text):
    words = text.split()
    num_words = (len(words))
    return num_words

def counting_characters(text):
    char_counts = {}
    for character in text:
        lower_case_character = character.lower()
        if lower_case_character in char_counts:
            char_counts[lower_case_character] += 1
        else:
            char_counts[lower_case_character] = 1    
    return char_counts
    
def sorting_dictionary(items):
    for item in items:
        is_alphabetical = item.isalpha()
        item.sort(reverse=True, key=sorting_dictionary)
    return items["num"]

def sort_characters(char_counts):
    char_list = []
    # loop dan append
    for char in char_counts:
        char_list.append({"char": char, "num": char_counts[char]})
    char_list.sort(key = lambda item: item["num"], reverse=True)
    return char_list