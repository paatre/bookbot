import sys
from stats import count_characters, count_words, get_sorted_character_counts


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    frankenstein = get_book_text(filepath)
    num_words = count_words(frankenstein)
    char_counts = count_characters(frankenstein)
    character_nums = get_sorted_character_counts(frankenstein)

    print(f"{num_words} words found in the document")
    print(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in character_nums:
        char = entry["char"]
        num = entry["num"]
        print(f"{char}: {num}")

    print("============= END ===============")


main()
