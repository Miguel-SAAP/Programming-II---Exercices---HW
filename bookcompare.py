import requests
from collections import Counter
import re

def get_book_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def clean_text(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return words

def count_unique_words(words):
    return len(set(words))

def main():
    book1_url = "https://www.gutenberg.org/cache/epub/84/pg84.txt"
    book2_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"

    # Fetch and process the books
    text1 = get_book_text(book1_url)
    text2 = get_book_text(book2_url)

    words1 = clean_text(text1)
    words2 = clean_text(text2)

    unique_words1 = count_unique_words(words1)
    unique_words2 = count_unique_words(words2)

    print(f"Unique words in Frankenstein: {unique_words1}")
    print(f"Unique words in Pride and Prejudice: {unique_words2}")

    if unique_words1 > unique_words2:
        print("Mary Shelley used more unique words.")
    else:
        print("Jane Austen used more unique words.")

if __name__ == "__main__":
    main()