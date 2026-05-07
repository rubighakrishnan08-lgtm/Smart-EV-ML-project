from data.synthetic_data import generate_ev_data # type: ignore
import numpy as np
from ..ml.grid_model import GridModel

data = generate_ev_data(200)

data["voltage"] = np.random.normal(230, 10, len(data))
data["current"] = np.random.normal(50, 15, len(data))
data["load"] = data["voltage"] * data["current"] / 1000

data["stress"] = (data["load"] > 10).astype(int)

X = data[["voltage", "current", "load"]]
y = data["stress"]

model = GridModel()
model.train(X, y)

print("ML Model trained!")