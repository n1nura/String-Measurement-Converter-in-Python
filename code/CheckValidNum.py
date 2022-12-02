from InputHandler import InputHandler


def CheckValidNum():
    # Identifies whether a number in a given string is valid or not
    print("Any value between -1000 and 1000 is valid\n")
    RawString = InputHandler()
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
