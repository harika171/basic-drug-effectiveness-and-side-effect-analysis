import pandas as pd

data = pd.read_csv(r"C:\Users\Harika\OneDrive\Documents\healthcare project\Book1.csv")

print(data.isnull().sum())

data.head(5)

# basic EDA

data.describe()

effectiveness_by_drug = data.groupby('Drug Name')['Effectiveness (1-5)'].mean()

print(effectiveness_by_drug)

data['User Rating'].value_counts()

#data visualization

import matplotlib.pyplot as plt
import seaborn as sns

# bar plot for average drug effectiveness
effectiveness_by_drug.plot(kind = 'bar', color = 'pink', figsize = (10,6))
plt.title('Average Drug Effectiveness')
plt.ylabel('Average Drug Effectiveness')
plt.xlabel('Drug Name')
plt.xticks(rotation = 45)
plt.show()

# pie chart for side effects distribution

side_effects_split = data['Side Effects'].str.split(', ').explode()
side_effects_count = side_effects_split.value_counts() 

side_effects_count.plot(kind = 'pie', autopct = '%1.1f%%', figsize = (8,8))
plt.title('Distribution of side Effects')
plt.ylabel;(' ')
plt.show()


#box plot user rating distribution

sns.boxplot(x = data['User Rating'],color = 'magenta')
plt.title('User Rating Distribution')
plt.show()
