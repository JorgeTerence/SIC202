from pandas import read_csv
import pandas as pd
import numpy as np

df = read_csv("data.csv")
df["Const"] = np.ones(df.shape[0])

cols = ["Const", "Pressure", "Angle"]  # Justificar exclusão da temperatura

X = np.array(df[cols])
Y = np.array(df["Distance"])

Xt = np.transpose(X)
XtX = np.matmul(Xt, X)
XtX_inv = np.linalg.inv(XtX)
XtY = np.matmul(Xt, Y)
coef = np.matmul(XtX_inv, XtY)
X_one = X

test = np.array([round(n, 2) for n in np.matmul(X, coef)])
diff = pd.DataFrame({"Tests": Y, "Results": test, "Diff": Y - test})

print(*cols)
print([round(c, 3) for c in coef.tolist()], "\n")
print(diff.head(), "\n")
print(f"Average diff: {(Y - test).mean()}")
