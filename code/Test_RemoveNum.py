from Test_ConvertCase import testConvertCase

def RemoveNum(RawString):
    # Removes Numerical Values from String and converts to upper or lower case.
    NumString = "0123456789"
    while not RawString.isdigit():
        remove_digits = str.maketrans('', '', NumString)
        result = RawString.translate(remove_digits)
        RawString = result
        finalStr = testConvertCase2(RawString)
        return finalStr
    print("String must contain at least one letter from A-Z")
    raise SystemExit

test1 = RemoveNum("Kanakaratne")
assert test1 == "kanakaratne"