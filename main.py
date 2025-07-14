import sys
from stats import get_num_words, counting_characters, sort_characters
# path_to_file = "/home/akutokyo/workspace/github.com/madwichery/bookbot/books/frankenstein.txt"



def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(book_path):
    text_from = get_book_text(book_path)
    num_words = get_num_words(text_from)
    print(f"{num_words} words found in the document")

    char_counts = counting_characters(text_from)

    sorted_chars = sort_characters(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ==============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    main(path_to_file)
    
