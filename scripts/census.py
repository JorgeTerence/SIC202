import pandas as pd

df = pd.read_csv("data/census.csv")

# Population from provinces 115 and 116
total = df[df["Province Code"].isin([115, 116])]["Population"].sum()
print(total)

# Average population from cities where there're more men than women
average = df[df["Gender Ratio"] < 1]["Population"].mean()
print(average)

# Places where `GenderRatio` > 1 and there's less than 2 people per house
places = df[df["Gender Ratio"] > 1]
lonely = places[places["Person's Household"] < 2]
print(lonely)

# Sort `df` based on `Households` in ascending order and show the first 10 entries
print(df.sort_values(by="Households").head())
