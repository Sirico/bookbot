from collections import Counter

book = "books/frankenstien.txt"
with open(book) as book:
    text = book.read()
    word_count = len(text.split())
    lower_string = text.lower()
    character_count = len(lower_string)
    book_title = book.name

    print(f"Starting report of book: {book_title}")
    print(f"{word_count} words found in the book")
    print(f"{character_count} characters found in the book")
    print()

    letter_count = Counter(lower_string)
    for letter, count in sorted(letter_count.items()):
        if letter.isalpha():
            print(f"The {letter} character was found: {count} times")
