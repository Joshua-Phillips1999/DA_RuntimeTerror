import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re

Menu=pd.read_csv("menu.csv")
#just a basic representation of how calories are distributed in the dataset
plt.hist(Menu.Calories)
plt.show()
#print('Summary Statistics for Calories: {}'.format(Menu['Calories'].describe()))
#to show what has the highest calories
HighCalorie = Menu.query('Calories > 1500')
print("\nHighest calorie\n\n",HighCalorie['Item'].head(5))
#to show what has the lowest calories
LowCalorie = Menu.query('Calories < 10')
print("\nLowest calories\n\n",LowCalorie['Item'].head(5))
#to group all foods by category and plot avg calorie count of items in group
Calories = Menu.drop('Item', axis = 1)
Calories = Menu.groupby(["Category"])["Calories"].mean()
Calories = Calories.sort_values(ascending=False)
print(Calories)

Category = ['Chicken & Fish', 'Smoothies & Shakes', 'Breakfast',
'Beef & Pork', 'Coffee & Tea', 'Salads', 'Snacks & Sides','Desserts','Beverages']

plt.figure(figsize = (20,10))
plt.suptitle('Calories by Category', fontsize = 24)
plt.xlabel('Category', fontsize = 20)
plt.ylabel("Calories", fontsize = 20)
plt.bar(Category, Calories)
plt.show()
#to find out how each of the variables are corelated to each other
corr = Menu.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True)
plt.title("McD Correlation Heatmap")

plt.show()
