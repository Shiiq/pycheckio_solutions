# This is pretty much a technical mission.
# You have raw HTTP cookies.
# Your mission is to extract the value of a specific cookie by its name.
# Input: Two arguments. Both are strings.
# The first one is the string of raw cookies, and the second one is the name of the cookie we are looking for.
#
# Output: A string. Extracted value.
#
# Example:
# get_cookie('theme=light; sessionToken=abc123', 'theme') == 'light'
# get_cookie('_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true', 'ffo') == 'true'


def parse_cookies(cookie_str):
    normalized_string = cookie_str.strip().split(";")
    parsed_cookies = dict([p.strip().split("=", maxsplit=1) for p in normalized_string])
    return parsed_cookies


def get_cookie(cookie, name):
    parsed_cookies = parse_cookies(cookie)
    return parsed_cookies.get(name)


if __name__ == "__main__":
    assert (
        get_cookie("theme=light; sessionToken=abc123", "theme") == "light"
    ), "theme=light"
    assert (
        get_cookie("_ga=GA1.2.447610749.1465220820; _gat=1; ffo=true", "ffo") == "true"
    ), "ffo=true"
    print("Looks like you know everything. It is time for 'Check'!")


