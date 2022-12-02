def ConvertCase(RawString):
    # Converts given string to upper or lower case
    while not RawString.isdigit():
        try:
            print("Choose Conversion\n1. Upper Case\n2. Lower Case")
            InputChoice = input("Type 1 or 2 and Press Enter:\n")
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
                ConvertCase()
        except ValueError:
            print("Something went wrong")
    print("String must contain at least one letter from A-Z")
    raise SystemExit
