# tests for instances of user choosing upper case
def testConvertCase(RawString):
    # Converts given string to upper or lower case
    while not RawString.isdigit():
        try:
            print("Choose Conversion\n1. Upper Case\n2. Lower Case")
            InputChoice = "1"
            if InputChoice == "1":
                ConvertedString = RawString.upper()
                print(ConvertedString)
                return ConvertedString

            elif InputChoice == "2":
                ConvertedString = RawString.lower()
                print(ConvertedString)
                return ConvertedString

            else:
                print("Invalid Selection.\n")
                testConvertCase()
        except ValueError:
            print("Something went wrong")
    print("String must contain at least one letter from A-Z")
    raise SystemExit


# tests for instances of user choosing lower case
def testConvertCase2(RawString):
    # Converts given string to upper or lower case
    while not RawString.isdigit():
        try:
            print("Choose Conversion\n1. Upper Case\n2. Lower Case")
            InputChoice = "2"
            if InputChoice == "1":
                ConvertedString = RawString.upper()
                print(ConvertedString)
                return ConvertedString

            elif InputChoice == "2":
                ConvertedString = RawString.lower()
                print(ConvertedString)
                return ConvertedString

            else:
                print("Invalid Selection.\n")
                testConvertCase2()
        except ValueError:
            print("Something went wrong")
    print("String must contain at least one letter from A-Z")
    raise SystemExit


test = testConvertCase("Kanakaratne")
assert test == "KANAKARATNE"

test2 = testConvertCase2("Kanakaratne")
assert test2 == "kanakaratne"

test3 = testConvertCase("aBc9488")
assert test3 == "ABC9488"

test4 = testConvertCase2("aBc9488")
assert test4 == "abc9488"

#test5 = testConvertCase("9488")
#assert test5 == "Error"
#produces Error

#test6 = testConvertCase("!")
#assert test6 == "String must contain at least one letter from A-Z"
#produces Error

test7 = testConvertCase("Ninura B.D.S. Kanakaratne")
assert test7 == "NINURA B.D.S. KANAKARATNE"

test8 = testConvertCase2("Ninura B.D.S. Kanakaratne")
assert test8 == "ninura b.d.s. kanakaratne"

test9 = testConvertCase("2001: A Space Odyssey")
assert test9 == "2001: A SPACE ODYSSEY"

test10 = testConvertCase2("2001: A Space Odyssey")
assert test10 == "2001: a space odyssey"

