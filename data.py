from string import punctuation


def get_words(book):
    """Make a list from all the words in a text file"""

    all_words = []

    try:
        a_file = open(book)
        for line in a_file:
            all_words.extend(line.rstrip().split())
    except:
        all_words.extend(book.rstrip().split())

    return all_words


def count_words(lst):
    """Make a dictionary where each word is they key and its value
       is the number of occurences in the text
    """

    word_count = {}

    for word in lst:
        word = word.strip(punctuation).lower()
        if '--' not in word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count.items()
