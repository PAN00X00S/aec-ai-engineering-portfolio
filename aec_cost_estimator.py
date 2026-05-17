def calculate_areas(length, width, height):
    floor_area = length * width
    wall_area = 2 * (length + width) * height
    return floor_area, wall_area

def estimate_cost(floor_area, wall_area, material):
    costs = {
        "drywall": {"floor": 0, "wall": 2.50},
        "tile": {"floor": 8.00, "wall": 12.00},
        "concrete": {"floor": 5.00, "wall": 0}
    }
    
    if material not in costs:
        return None
    
    floor_cost = floor_area * costs[material]["floor"]
    wall_cost = wall_area * costs[material]["wall"]
    return floor_cost, wall_cost

def main():
    print("\n=== AEC Project Cost Estimator ===")
    
    length = float(input("Room length (ft): "))
    width = float(input("Room width (ft): "))
    height = float(input("Ceiling height (ft): "))
    
    print("\nMaterial options: drywall, tile, concrete")
    material = input("Select material: ").lower()
    
    floor_area, wall_area = calculate_areas(length, width, height)
    result = estimate_cost(floor_area, wall_area, material)
    
    if result is None:
        print("Invalid material selected.")
        return
    
    floor_cost, wall_cost = result
    total = floor_cost + wall_cost
    
    print(f"\n=== ESTIMATE REPORT ===")
    print(f"Floor area:   {floor_area:.1f} sqft")
    print(f"Wall area:    {wall_area:.1f} sqft")
    print(f"Floor cost:   ${floor_cost:.2f}")
    print(f"Wall cost:    ${wall_cost:.2f}")
    print(f"TOTAL:        ${total:.2f}")

main()
