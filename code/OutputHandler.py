def OutputHandler(OutputVal):
    print("Save to File?")
    SaveChoice = input("Y/N\n")
    if SaveChoice == "Y" or SaveChoice == "y":
        file = open("..\\documents\\OutputFile.txt", "a")
        file.write("\n")
        file.write(OutputVal)
        file.close()
    elif SaveChoice == "N" or SaveChoice == "n":
        print("Output was not Saved")
    else:
        print("Invalid Selection")
