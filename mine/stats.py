def get_num_words(file_contents):
    words = file_contents.split()
    return f"{len(words)} words found in the document"