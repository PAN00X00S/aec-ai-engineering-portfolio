def feet_to_meters(feet):
    return feet * 0.3048


def meters_to_feet(meters):
    return meters / 0.3048


def sqft_to_sqm(sqft):
    return sqft * 0.092903


print("AEC Unit Converter")
print("==================")
feet = float(input("Enter feet: "))
print(f"{feet} ft = {feet_to_meters(feet):.3f} m")
