def convert_units(value, unit_type):
    if unit_type == "meters to kilometers":
        return value / 1000
    elif unit_type == "grams to kilograms":
        return value / 1000
    else:
        return "Conversion not supported"

value = float(input("Enter value: "))
unit_type = input("Enter unit type (meters to kilometers / grams to kilograms): ")
print(f"Converted value: {convert_units(value, unit_type)}")
