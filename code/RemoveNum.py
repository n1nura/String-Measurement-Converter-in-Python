from InputHandler import InputHandler
from ConvertCase import ConvertCase


def RemoveNum():
    # Removes Numerical Values from String and converts to upper or lower case.
    RawString = InputHandler()
    NumString = "0123456789"
    while not RawString.isdigit():
        remove_digits = str.maketrans('', '', NumString)
        result = RawString.translate(remove_digits)
        RawString = result
        finalStr = ConvertCase(RawString)
        return finalStr
    print("String must contain at least one letter from A-Z")
    raise SystemExit