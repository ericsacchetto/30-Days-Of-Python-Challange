import pandas as pd

hacker_file = '..\data\hacker_news.csv'
df = pd.read_csv(hacker_file)
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(f"python occurrences in title: {df['title'].str.contains('python').sum()}")
print(f"JavaScript occurrences in title: {df['title'].str.contains('JavaScript').sum()}")
