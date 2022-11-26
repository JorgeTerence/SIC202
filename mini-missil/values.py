from pandas import read_csv
import pandas as pd
import numpy as np

def coef(df: pd.DataFrame, cols: list[str], res: str) -> np.ndarray:
    df = df.copy()
    df["Const"] = np.ones(df.shape[0])

    x = np.array(df[["Const"] + cols])
    y = np.array(df[res])

    xt = np.transpose(x)
    xtx = np.matmul(xt, x)
    xtx_inv = np.linalg.inv(xtx)
    xty = np.matmul(xt, y)

    return np.matmul(xtx_inv, xty) # coeficients


df = read_csv("data.csv")

cols = ["Pressure", "Angle"]

coeficients = coef(df, ["Pressure", "Angle"], "Distance")

print("Const", *cols)
# print([round(c, 3) for c in coeficients], "\n")
print(coeficients)
