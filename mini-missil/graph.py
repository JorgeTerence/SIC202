import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def draw():
    df = pd.read_csv("data.csv")

    ax = plt.axes(projection="3d")

    for row in np.array(df[["Pressure", "Angle", "Distance"]]):
        ax.scatter(*row)

    ax.set_xlabel("P")
    ax.set_ylabel("θ")
    ax.set_zlabel("s")

    return ax

if __name__ == "__main__":
    draw()
    plt.show()
