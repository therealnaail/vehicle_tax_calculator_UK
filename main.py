def calc_tax(emissions, fuel_type):
    if fuel_type == "Petrol" or "Diesel":
        if emissions >= 0 and emissions <= 50:
            return 10
        elif emissions >= 51 and emissions <= 75:
            return 25
        elif emissions >= 76 and emissions <= 90:
            return 120
        elif emissions >= 91 and emissions <= 100:
            return 150
        elif emissions >= 101 and emissions <= 110:
            return 170
        elif emissions >= 111 and emissions <= 130:
            return 190
        elif emissions >= 131 and emissions <= 150:
            return 230
        elif emissions >= 151 and emissions <= 170:
            return 585
        elif emissions >= 171 and emissions <= 190:
            return 945
        elif emissions >= 191 and emissions <= 225:
            return 1420
        elif emissions >= 226 and emissions <= 255:
            return 2015
        elif emissions > 255:
            return 2365
    elif fuel_type == "Electric":
        return 0
    elif fuel_type == "Alternative":
        if emissions >= 0 and emissions <= 50:
            return 0
        elif emissions >= 51 and emissions <= 75:
            return 15
        elif emissions >= 76 and emissions <= 90:
            return 110
        elif emissions >= 91 and emissions <= 100:
            return 140
        elif emissions >= 101 and emissions <= 110:
            return 160
        elif emissions >= 111 and emissions <= 130:
            return 180
        elif emissions >= 131 and emissions <= 150:
            return 220
        elif emissions >= 151 and emissions <= 170:
            return 575
        elif emissions >= 171 and emissions <= 190:
            return 935
        elif emissions >= 191 and emissions <= 225:
            return 1410
        elif emissions >= 226 and emissions <= 255:
            return 2005
        elif emissions > 255:
            return 2355
    else:
        return "Invalid fuel type"

def calc_second_tax(fuel_type):
    if fuel_type == "petrol" or fuel_type == "diesel":
        return 165
    elif fuel_type == "electric":
        return 0
    else:
        return 155
print("UK vehicle tax calculator by therealnaail (information from gov.uk/vehicle-tax-rate-tables)")
emissions = int(input("Enter the CO2 emissions of your vehicle in g/km: "))
fuel_type = input("Enter the fuel type of your vehicle (Petrol, Diesel, Electric or Alternative): ")

first_tax = calc_tax(emissions, fuel_type)
second_tax = calc_second_tax(fuel_type)

if type(first_tax) and type(second_tax) == int:
    print("Your vehicle's first tax payment is £" + str(first_tax))
    print("Your second tax payment onwards is £" + str(second_tax))
else:
    print(Error)
