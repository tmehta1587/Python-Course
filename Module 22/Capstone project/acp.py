
import panda as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("IMBD Dataset.csv")

print("First 3 rows:")
print(df.head(3))
print("\nLast 3 rows:")
print(df.tail(3))
      
print("\nDataset Info:")
print(df.info())

print("\nNull Values Check:")
print(df.insull().sum())

subset_df = df.iloc[40:75]
print("/nSubset (Rows 41-75):")
print(subset_df)

max_votes_movie = df[df['No_of_Votes']== df['No_of_Votes'].max()]
print("\nMovie with highest votes: ")
print(max_votes_movie)
