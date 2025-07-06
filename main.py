from stats import get_num_words
path_to_file = "/home/akutokyo/workspace/github.com/madwichery/bookbot/books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text_from = get_book_text(path_to_file)
    num_words = get_num_words(text_from)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()