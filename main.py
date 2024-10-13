import re


def read_book(book_path):
    with open(book_path, "r") as b:
        file_contents = b.read()
    return file_contents


def count_words(book):
    word_count = re.findall("\S+", book)
    return word_count


def count_characters(book):
    character_count = {}
    no_space_book = book.lower().replace(" ", "").replace("\n", "")
    for c in no_space_book:
        if c not in character_count.keys():
            character_count[c] = 1
        else:
            character_count[c] += 1
    return character_count


def main():
    book_content = read_book("books/frankenstein.txt")
    words_in_book = count_words(book_content)
    chars_in_book = count_characters(book_content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words_in_book)} words found in the document\n")
    for k, v in chars_in_book.items():
        print(f"The '{k}' character was found {v} times")


if __name__ == "__main__":
    main()
