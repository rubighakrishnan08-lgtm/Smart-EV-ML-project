import numpy as np
import pandas as pd

def generate_ev_data(n=20):
    return pd.DataFrame({
        "vehicle_id": range(n),
        "SoC": np.random.randint(10, 90, n),
        "distance": np.random.randint(5, 100, n),
        "profession": np.random.choice([1,2,3], n),  # 1 = high priority
        "emergency": np.random.choice([0,1], n, p=[0.8,0.2])
    })

def generate_grid():
    voltage = np.random.normal(230, 10)
    current = np.random.normal(50, 15)
    load = voltage * current / 1000
    return voltage, current, load

# Test
if __name__ == "__main__":
    print(generate_ev_data())
    print(generate_grid())


def generate_grid():
    voltage = np.random.normal(230, 10)
    current = np.random.normal(50, 15)
    load = voltage * current / 1000
    return voltage, current, load