# In this mission you need to create a password verification function.
# The verification conditions are:
# the length should be bigger than 6;
# should contain at least one digit.
# Input: A string.
# Output: A bool.


def is_acceptable_password(password):
    ln = 0
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
        ln += 1
    return (ln > 6 and digit)


if __name__ == '__main__':
    assert is_acceptable_password("short") == False
    assert is_acceptable_password("muchlonger") == False
    assert is_acceptable_password("ashort") == False
    assert is_acceptable_password("muchlonger5") == True
    assert is_acceptable_password("sh5") == False
    print("The mission is done! Click 'Check Solution' to earn rewards!")
