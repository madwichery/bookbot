path_to_file = "/home/akutokyo/workspace/github.com/madwichery/bookbot/books/frankenstein.txt"

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(get_book_text(path_to_file))

if __name__ == "__main__":
    main()