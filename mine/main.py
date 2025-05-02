import sys
from stats import get_num_words


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Get the book path from the command-line argument
    book_path = sys.argv[1]

    try:
        with open(book_path) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)

    print(f"--- Begin report of {book_path} ---")
    print(get_num_words(file_contents))
    dict = count_char(file_contents)
    for d, c in sorted(dict.items()):
        if not d.isalpha():
            continue
        print(f"The '{d}' character was found {c}")
    print("--- End report ---")


def count_char(contents):
    char_counts = {}
    for char in contents.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


if __name__ == "__main__":
    main()