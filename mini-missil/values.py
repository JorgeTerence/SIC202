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

    c = np.matmul(xtx_inv, xty) # coeficients

    print("Const", *cols, "->", res)
    print([round(n, 3) for n in c])
    print()

    return c


df = read_csv("data.csv")

cols = ["Pressure", "Angle"]

coef(df, ["Pressure", "Angle"], "Distance") # Preview distance

coef(df, ["Distance", "Pressure"], "Angle") # Calculate angle
