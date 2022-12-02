from InputHandler import InputHandler


def ConvertMeasureUnit():
    m_ft_convert = 3.281
    cm_in_convert = 2.54
    print("Enter Measurement")
    Measurement = InputHandler()
    print("Select conversion:\n1. m to ft\n2. ft to m\n3. cm to in\n4. in to c\n")
    UnitChoice = input("Enter corresponding number:\n")
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