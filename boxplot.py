import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

#sns.set_theme(style="whitegrid")
menu=pd.read_csv("menu.csv")
ax=sns.boxplot(x=menu["Calories"])
plt.show()
b=sns.boxplot(x=menu['Total Fat'])
plt.show()
c=sns.boxplot(x=menu['Trans Fat'])
plt.show()
c=sns.boxplot(x=menu['Cholesterol'])
plt.show()
c=sns.boxplot(x=menu['Sodium'])
plt.show()
c=sns.boxplot(x=menu['Protein'])
plt.show()


