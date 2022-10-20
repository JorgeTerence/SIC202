import pandas as pd

df = pd.read_csv("data/students.csv")

male = df[df["Gender"] == "M"]
female = df[df["Gender"] == "F"]

print(f"Altura média M: {round(male['Height'].mean(), 2)}cm")
print(f"Altura média F: {round(female['Height'].mean(), 2)}cm\n")

print(f"Peso médio M: {round(male['Weight'].mean(), 2)}kg")
print(f"Peso médio F: {round(female['Weight'].mean(), 2)}kg\n")

print(f"Maior altura M: {round(male['Height'].max(), 2)}cm")
print(f"Menor altura F: {round(female['Height'].min(), 2)}cm\n")

male_weight = male[male["Height"] > 175]["Weight"].min()
female_weight = female[female["Height"] < 160]["Weight"].max()

print(f"Maior peso M com altura > 175cm: {male_weight}")
print(f"Maior peso F com altura < 160cm: {female_weight}\n")

cdf_average = df[df["Absence"] == "N"]["Grade"].mean()
tourists_average = df[df["Absence"] == "Y"]["Grade"].mean()

print(f"Nota média dos 100% presença: {round(cdf_average, 2)}")
print(f"Nota média dos turistas: {tourists_average}\n")

overall_height = df[df["Bloodtype"].str[0] == "A"]["Height"].mean()
male_height = male[male["Bloodtype"].str[0] == "A"]["Height"].mean()

print(f"Altura média de alunos do tipo sanguíneo A ou AB: {round(overall_height, 2)}")
print(f"Altura média M do tipo sanguíneo A ou AB: {round(male_height, 2)}\n")

good_tourists_average = df[(df["Absence"] == "Y") & (df["Grade"] > 3)]["Age"].mean()

print(f"Idade média dos turistas com nota acima de 3: {good_tourists_average}")
