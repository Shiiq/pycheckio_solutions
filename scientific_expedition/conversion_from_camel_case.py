def from_camel_case(name: str) -> str:
    # first
    # replace = lambda x: f"_{x.lower()}"
    # res = ""
    # res += name[0].lower()
    # for index, sym in enumerate(name[1:]):
    #     if sym.islower():
    #         res += sym
    #     elif sym.isupper():
    #         res += replace(sym)

    # second
    res = "".join(sym if sym.islower() else f"_{sym.lower()}" for sym in name)[1:]

    return res


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
