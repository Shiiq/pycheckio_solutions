# You have a text and a sequence of words.
# You need to check if the words in sequence appear in the same order as in the given text.
#
# Cases you should expect while solving this challenge:
#
# a word from the sequence is not in the text - your function should return False;
# any word can appear more than once in a text - use only the first one;
# two words in the given sequence are the same - your function should return False;
# the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
# the text includes only English letters and spaces.
# Input: Two arguments.
# The first one is a given text as a string (str), the second is list of words as strings (str).


def words_order(text: str, words: list):
    if len(words) == 1:
        return words[0] in text
    if len(set(words)) == 1:
        return False

    temp_storage = {}
    text = text.split()
    for word in words:
        for subw in text:
            pass
        pass

    # print(words, type(words))
    pass


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    # assert words_order('hi world im here', ['world', 'here']) == True
    # assert words_order('hi world im here', ['here', 'world']) == False
    # assert words_order('hi world im here', ['world']) == True
    # assert words_order('hi world im here',
    #                    ['world', 'here', 'hi']) == False
    # assert words_order('hi world im here',
    #                    ['world', 'im', 'here']) == True
    # assert words_order('hi world im here',
    #                    ['world', 'hi', 'here']) == False
    # assert words_order('hi world im here', ['world', 'world']) == False
    # assert words_order('hi world im here',
    #                    ['country', 'world']) == False
    # assert words_order('hi world im here', ['wo', 'rld']) == False
    # assert words_order('', ['world', 'here']) == False
    # print("Coding complete? Click 'Check' to earn cool rewards!")
    pass
