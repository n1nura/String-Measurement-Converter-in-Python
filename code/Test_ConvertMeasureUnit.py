def ConvertMeasureUnit(Measurement):
    m_ft_convert = 3.281
    cm_in_convert = 2.54
    #print("Enter Measurement")
    #print("Select conversion:\n1. m to ft\n2. ft to m\n3. cm to in\n4. in to c\n")
    UnitChoice = "1"
    try:
        if UnitChoice == "1":  # meters to feet
            Measurement = float(Measurement) * m_ft_convert
            str(Measurement)
            print(Measurement)
            return Measurement
        elif UnitChoice == "2":  # feet to meters
            Measurement = float(Measurement) / m_ft_convert
            str(Measurement)
            print(Measurement)
            return Measurement
        elif UnitChoice == "3":  # centimeters to inches
            Measurement = float(Measurement) / cm_in_convert
            str(Measurement)
            print(Measurement)
            return Measurement
        elif UnitChoice == "4":  # inches to centimeters
            Measurement = float(Measurement) * cm_in_convert
            str(Measurement)
            print(Measurement)
            return Measurement
        else:
            print("Invalid Selection")
            ConvertMeasureUnit()
    except ValueError:
        print("Invalid value. Only real numbers supported")
        return False


test1 = ConvertMeasureUnit("Kanakaratne")
assert test1 == False

test2 = ConvertMeasureUnit("aBc9488")
assert test2 == False

test3 = ConvertMeasureUnit("9488")
assert test3 == 31130.128

test4 = ConvertMeasureUnit("!")
assert test4 == False

test5 = ConvertMeasureUnit("Ninura B.D.S.Kanakaratne")
assert test5 == False

test6 = ConvertMeasureUnit("Kanakaratne")
assert test6 == False
