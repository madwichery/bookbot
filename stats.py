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