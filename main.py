path_to_file = "/home/akutokyo/workspace/github.com/madwichery/bookbot/books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def accept_text_as_string_return_number_of_words(text):
    words = text.split()
    num_words = (len(words))
    return num_words

def main():
    text_from = get_book_text(path_to_file)
    num_words = accept_text_as_string_return_number_of_words(text_from)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()