from aec_csv_reader import estimate_room, read_rooms
import csv

def get_room_input():
    print("\n--- Add a Room ---")
    name = input("Room name: ")
    length = input("Length (ft): ")
    width = input("Width (ft): ")
    height = input("Ceiling height (ft): ")
    print("Materials: drywall, tile, concrete")
    material = input("Material: ").lower()
    
    return {
        'room_name': name,
        'length': length,
        'width': width,
        'height': height,
        'material': material
    }

def save_to_csv(rooms, filename="custom_rooms.csv"):
    with open(filename, 'w', newline='') as f:
        fieldnames = ['room_name', 'length', 'width', 'height', 'material']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rooms)
    print(f"\nRooms saved to {filename}")

def save_report(results, grand_total):
    with open("custom_report.txt", "w") as f:
        f.write("=== ARCFORGE PROJECT REPORT ===\n\n")
        for r in results:
            f.write(f"{r['room']}\n")
            f.write(f"  Floor: {r['floor_area']:.0f} sqft\n")
            f.write(f"  Walls: {r['wall_area']:.0f} sqft\n")
            f.write(f"  Cost:  ${r['total']:.2f}\n\n")
        f.write(f"{'='*30}\n")
        f.write(f"PROJECT TOTAL: ${grand_total:.2f}\n")
    print("Report saved to custom_report.txt")

def main():
    print("\n=== ARCFORGE Room Builder ===")
    rooms = []
    
    while True:
        add = input("\nAdd a room? (y/n): ").lower()
        if add != 'y':
            break
        room = get_room_input()
        rooms.append(room)
        print(f"✓ {room['room_name']} added")
    
    if not rooms:
        print("No rooms added. Exiting.")
        return
    
    save_to_csv(rooms)
    
    print("\n=== ESTIMATE REPORT ===")
    results = []
    grand_total = 0
    for room in rooms:
        result = estimate_room(room)
        results.append(result)
        print(f"\n{result['room']}")
        print(f"  Floor: {result['floor_area']:.0f} sqft")
        print(f"  Walls: {result['wall_area']:.0f} sqft")
        print(f"  Cost:  ${result['total']:.2f}")
        grand_total += result['total']
    
    print(f"\n{'='*30}")
    print(f"PROJECT TOTAL: ${grand_total:.2f}")
    save_report(results, grand_total)

main()