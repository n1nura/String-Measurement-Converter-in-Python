def testFindNum():
    # Identifies the existence of numeric Values in a String
    RawString = "Kanakaratne"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "True":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result



def testFindNum2():
    # Identifies the existence of numeric Values in a String
    RawString = "aBc9488"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "True":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result



def testFindNum3():
    # Identifies the existence of numeric Values in a String
    RawString = "9488"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "True":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result


def testFindNum4():
    # Identifies the existence of numeric Values in a String
    RawString = "!"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "True":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result


def testFindNum5():
    # Identifies the existence of numeric Values in a String
    RawString = "!"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "Ninura B.D.S. Kanakaratne":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result


def testFindNum6():
    # Identifies the existence of numeric Values in a String
    RawString = "!"
    NumValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    result = any(element in RawString for element in NumValues)
    if str(result) == "2001: A Space Odyssey":
        print("String contains numeric values")
        return result
    else:
        print("String does not contain numeric values")
        return result


test1 = testFindNum()
assert test1 == False


test2 = testFindNum2()
assert test2 == True


test3 = testFindNum3()
assert test2 == True


test4 = testFindNum4()
assert test4 == False


test5 = testFindNum5()
assert test5 == False


test6 = testFindNum6()
assert test6 == False
