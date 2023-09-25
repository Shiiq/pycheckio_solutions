# You are given a text, which contains different English letters
# and punctuation symbols. You should find the most frequent letter
# in the text. The letter returned must be in lower case.

# While checking for the most wanted letter, casing does not matter,
# so for the purpose of your search, "A" == "a".
# Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

# If you have two or more letters with the same frequency,
# then return the letter which comes first in the Latin alphabet.
# For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

# Input: A text for analysis as a string (str).
# Output: The most frequent letter in lower case as a string (str).

# Examples:
# assert checkio("Hello World!") == "l"
# assert checkio("How do you do?") == "o"
# assert checkio("One") == "e"
# assert checkio("Oops!") == "o"
# How it is used: For most decryption tasks you need to know the frequency
# of occurrence for various letters in a section of text.
# For example: we can easily crack a simple addition or substitution
# cipher if we know the frequency in which letters appear.
# This is interesting stuff for language experts
from functools import reduce


def get_max(a, b):
    if a[1] > b[1]:
        return a
    elif a[1] == b[1]:
        if a[0] < b[0]:
            return a
    return b


def analyze_input(input_str: str):
    d = dict()
    input_str = input_str.lower()
    for l in input_str:
        if 97 <= ord(l) <= 120:
            v = d.setdefault(ord(l), 0)
            d[ord(l)] = v + 1
    return d


def checkio(input_data):
    items = analyze_input(input_data)
    most_want = reduce(get_max, items.items())
    print(input_data, chr(most_want[0]))
    return chr(most_want[0])

# TODO check case with upper/lower cases
if __name__ == "__main__":
    assert checkio("Hello World!") == "l"
    assert checkio("How do you do?") == "o"
    assert checkio("One") == "e"
    assert checkio("Oops!") == "o"
    assert checkio('Z') == 'z'
    print("Done!")
