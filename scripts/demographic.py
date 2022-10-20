import pandas as pd

df = pd.read_csv("data/demographics.csv")

# Time spent online by girls, on average
average = df[df["Sexo"] == "F"]["Internet"].mean()
print(f"Girls spent, on average: {round(average, 1)} hours online")

# Boys' average grade
average = df[df["Sexo"] == "M"]["Notas"].mean()
print(f"Boys' average grade was {round(average, 1)}")

# Average friend count
average = df["Amigos"].mean()
print(f"People have, on average, {round(average, 1)} friends")

# Average age for a Palmeiras fan
average = df[df["Time"] == "PALMEIRAS"]["Idade"].mean()
print(f"Palmeiras fans are, on average, {round(average, 1)} years old")

# Average friend count of a K-Pop fan
average = df[df["Banda"] == "KPOP"]["Amigos"].mean()
print(f"K-Pop fans have, on average, {round(average, 1)} friends")

# Average grade of Pink Floyd fans
average = df[df["Banda"] == "PINK FLOYD"]["Notas"].mean()
print(f"Pink Floyd fans' average grade was {round(average, 1)}")

# Age of the oldest Palmeiras fan whos also a Patati e Patatá fan
oldest = df[df["Time"] == "PALMEIRAS"]["Idade"].max()
print(f"The oldest fan of Palmeiras and Patati & Patata is {oldest} years old")

# Women's average age
average = df[df["Sexo"] == "F"]["Idade"].mean()
print(f"Sampled women are, on average, {round(average, 1)} years old")
