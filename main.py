
from stats import get_num_words, get_num_letters, dict_to_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    path = book_path

    name_with_ext = path.split("/")[-1]
    stem = name_with_ext.split(".")[0]



    word_count, text = get_num_words(stem)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    char_counts = get_num_letters(text)
    clean_count = dict_to_list(char_counts)

    for item in clean_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()