#Written by Ninura Kanakaratne

from InputHandler import InputHandler
from ConvertCase import ConvertCase
from FindNum import FindNum
from CheckValidNum import CheckValidNum
from RemoveNum import RemoveNum
from ConvertMeasureUnit import ConvertMeasureUnit
from OutputHandler import OutputHandler


def main():
    print("Please select one of the following\n")

    CatChoice = input("Type 1 for String Conversions. Type 2 for Measurement Conversions.\n")

    if CatChoice == "1":
        print("Select one of the following String conversion operations by typing the corresponding number\n")

        StrChoice = input("1. Convert to Upper/Lower Case.\n2. Find existence of numbers in string.\n3. Check "
                          "validity of number in string.\n4. Remove numbers in string.\n")
        match StrChoice:
            case "1":
                OutputHandler(ConvertCase(InputHandler()))
            case "2":
                FindNum()
            case "3":
                CheckValidNum()
            case "4":
                OutputHandler(RemoveNum())
            case other:
                print("Invalid Selection")
                main()

    elif CatChoice == "2":
        OutputHandler(str(ConvertMeasureUnit()))

    else:
        print("Invalid Choice")
        main()


if __name__ == "__main__":
    main()
