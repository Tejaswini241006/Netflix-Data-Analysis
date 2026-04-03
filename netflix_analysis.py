import pandas as pd

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Show first rows
print(df.head())
print(df.info())
print(df.isnull().sum())
df.dropna(inplace=True)
print(df.shape)
print(df['type'].value_counts())

import matplotlib.pyplot as plt

df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.show()

print(df['country'].value_counts().head(10))
df['country'].value_counts().head(10).plot(kind='barh')
plt.title("Top 10 Countries")
plt.show()

df['release_year'].value_counts().sort_index().plot()
plt.title("Content Released Over Years")
plt.show()

print(df['rating'].value_counts().head(5))
