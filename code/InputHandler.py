def InputHandler():
    print("Choose Input Method\n1. Manual Input\n2. Read from file ")
    InputChoice = input("Type 1 or 2 and Press Enter:\n")
    if InputChoice == "1":
        RawString = input("Enter String:\n")
        return RawString

    elif InputChoice == "2":
        file = open("..\\documents\\InputFile.txt")
        RawString = file.readline()
        return RawString

    else:
        print("Invalid Selection.\n")
        InputHandler()
