from fastapi import FastAPI
from aec_csv_reader import read_rooms, estimate_room

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AEC Cost Estimator API", "status": "running"}

@app.get("/estimate")
def estimate():
    rooms = read_rooms("rooms.csv")
    
    results = []
    grand_total = 0
    
    for room in rooms:
        result = estimate_room(room)
        results.append(result)
        grand_total += result['total']
    
    return {
        "project_total": grand_total,
        "rooms": results
    }