from fastapi import FastAPI
from ..data.synthetic_data import generate_ev_data, generate_grid

app = FastAPI()

@app.get("/simulate")
def simulate():
    ev_data = generate_ev_data()
    voltage, current, load = generate_grid()

    return {
        "ev_data": ev_data.to_dict(),
        "grid": {
            "voltage": voltage,
            "current": current,
            "load": load
        }
    }