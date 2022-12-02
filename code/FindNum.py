from InputHandler import InputHandler


def FindNum():
    # Identifies the existence of numeric Values in a String
    RawString = InputHandler()
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "True":
        print("String contains numeric values")
    else:
        print("String does not contain numeric values")
