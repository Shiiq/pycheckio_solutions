# In a given string you should reverse every word, but the words should stay in their places.
# Input: A string (str).
# Output: A string (str).
# Examples:
# assert backward_string_by_word("") == ""
# assert backward_string_by_word("world") == "dlrow"
# assert backward_string_by_word("hello world") == "olleh dlrow"
# assert backward_string_by_word("hello   world") == "olleh   dlrow"


def backward_string_by_word(text: str) -> str:

    result_data = ""
    spaces_pos = []
    l = len(text)

    for i, v in enumerate(text):
        if v.isspace():
            spaces_pos.append(i)

    words_rev = [i for i in text.split()[::-1]]
    words_rev = [l for w in words_rev for l in w]

    for i in range(l):
        if i in spaces_pos:
            result_data += " "
        else:
            letter = words_rev.pop()
            result_data += letter
    return result_data


if __name__ == '__main__':
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
