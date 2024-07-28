def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print (count_words(file_contents))
    dict = count_char(file_contents)
    for d,c in sorted(dict.items()):
        if not d.isalpha():
            continue
        print (f"The '{d}' character was found {c}")
    print("--- End report ---")
    
def count_words(file_contents):
    words = file_contents.split()
    return f"{len(words)} words in the given file."

def count_char(contents):
    char_counts = {}
    for char in contents.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

main()