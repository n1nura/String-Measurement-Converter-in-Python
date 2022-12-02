def CheckValidNum(RawString):
    # Identifies whether a number in a given string is valid or not
    print("Any value between -1000 and 1000 is valid\n")
    ValidNum = True
    try:
        float(RawString)
    except ValueError:
        ValidNum = False
        return ValidNum
    if ValidNum and -1000 <= float(RawString) <= 1000:
        print("Valid Number")
        return ValidNum
    else:
        print("Invalid Number")
        ValidNum = False
        return ValidNum



test1 = CheckValidNum("Kanakaratne")
assert test1 == False

test2 = CheckValidNum("aBc9488")
assert test2 == False

test3 = CheckValidNum("400")
assert test3 == True

test4 = CheckValidNum("9488")
assert test4 == False

test5 = CheckValidNum("!")
assert test5 == False

test6 = CheckValidNum("Ninura B.D.S.Kanakaratne")
assert test6 == False

test7 = CheckValidNum("2001: A Space Odyssey ")
assert test7 == False

test8 = CheckValidNum("1000")
assert test8 == True

test9 = CheckValidNum("-1000.1")
assert test9 == False

