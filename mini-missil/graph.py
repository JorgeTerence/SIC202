import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

for row in np.array(df[["Pressure", "Angle", "Distance"]]):
    ax.scatter(*row)

ax.set_xlabel("P")
ax.set_ylabel("θ")
ax.set_zlabel("d")

plt.show()
