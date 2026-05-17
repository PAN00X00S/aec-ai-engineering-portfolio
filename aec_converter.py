def feet_to_meters(feet):
    return feet * 0.3048

def meters_to_feet(meters):
    return meters / 0.3048

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqm_to_sqft(sqm):
    return sqm / 0.092903

def inches_to_mm(inches):
    return inches * 25.4

def mm_to_inches(mm):
    return mm / 25.4

def main():
    while True:
        print("\n=== AEC Unit Converter ===")
        print("1. Feet → Meters")
        print("2. Meters → Feet")
        print("3. Sq Ft → Sq Meters")
        print("4. Sq Meters → Sq Ft")
        print("5. Inches → Millimeters")
        print("6. Millimeters → Inches")
        print("0. Exit")
        
        choice = input("\nSelect option: ")
        
        if choice == "0":
            print("Goodbye.")
            break
        elif choice == "1":
            val = float(input("Enter feet: "))
            print(f"{val} ft = {feet_to_meters(val):.3f} m")
        elif choice == "2":
            val = float(input("Enter meters: "))
            print(f"{val} m = {meters_to_feet(val):.3f} ft")
        elif choice == "3":
            val = float(input("Enter sq ft: "))
            print(f"{val} sqft = {sqft_to_sqm(val):.3f} sqm")
        elif choice == "4":
            val = float(input("Enter sq meters: "))
            print(f"{val} sqm = {sqm_to_sqft(val):.3f} sqft")
        elif choice == "5":
            val = float(input("Enter inches: "))
            print(f"{val} in = {inches_to_mm(val):.1f} mm")
        elif choice == "6":
            val = float(input("Enter mm: "))
            print(f"{val} mm = {mm_to_inches(val):.3f} in")
        else:
            print("Invalid option. Try again.")

            
main()