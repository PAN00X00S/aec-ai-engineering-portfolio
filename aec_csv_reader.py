import csv

def read_rooms(filename):
    rooms = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rooms.append(row)
    return rooms

def estimate_room(room):
    costs = {
        "drywall": {"floor": 0, "wall": 2.50},
        "tile": {"floor": 8.00, "wall": 12.00},
        "concrete": {"floor": 5.00, "wall": 0}
    }
    
    length = float(room['length'])
    width = float(room['width'])
    height = float(room['height'])
    material = room['material']
    
    floor_area = length * width
    wall_area = 2 * (length + width) * height
    
    floor_cost = floor_area * costs[material]["floor"]
    wall_cost = wall_area * costs[material]["wall"]
    total = floor_cost + wall_cost
    
    return {
        "room": room['room_name'],
        "floor_area": floor_area,
        "wall_area": wall_area,
        "total": total
    }

def main():
    print("\n=== AEC CSV Cost Estimator ===")
    rooms = read_rooms("rooms.csv")
    
    grand_total = 0
    for room in rooms:
        result = estimate_room(room)
        print(f"\n{result['room']}")
        print(f"  Floor: {result['floor_area']:.0f} sqft")
        print(f"  Walls: {result['wall_area']:.0f} sqft")
        print(f"  Cost:  ${result['total']:.2f}")
        grand_total += result['total']
    
    print(f"\n{'='*30}")
    print(f"PROJECT TOTAL: ${grand_total:.2f}")

main()