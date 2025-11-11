
import pandas as pd
import seaborn as sns
sns.set(color_codes=True)

weather = pd.read_csv(r"C:\Users\Tinashe Mehta\New folder\Python Course\Module 22\Advance Visualizations in Python\weather.csv")
print(weather.head())

print(weather.info())

print(sns.barplot(weather['humidity'], weather['temperature']))

print(sns.distplot(weather['humidity']))

print(sns.distplot(weather['humidity'], kde=False, rug=True))

print(sns.jointplot(weather['humidity'], weather['temperature']))

print(sns.jointplot(weather['humidity'], weather['temperature']))

print(sns.jointplot(weather['humidity'], weather['temperature'], kind="hex"))

print(sns.jointplot(weather['humidity'], weather['temperature'], kind="kde"))
