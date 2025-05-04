import sys
from stats import get_word_count, get_char_count, sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(text)
    sorted_char_count = sort_dict(char_count)
    for char_data in sorted_char_count:
        print(f"{char_data['char']}: {char_data['count']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()