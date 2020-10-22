import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data=pd.read_csv("menu.csv")
df=pd.read_csv("menu_incomplete.csv")
df.info()
new_data = df.dropna(axis = 0, how ='all')  
# filtering data   
#print(new_data)  
#print(data)

print("Old data frame length:", len(df)) 
print("New data frame length:", len(new_data))  
print("Number of rows with all NA value: ", (len(df)-len(new_data))) 
#new_data["MinTemp"].fillna( method ='ffill', inplace = True) 

#sns.heatmap(data.isnull())
#plt.show()

# replacing the NA vaules of numeric columns with the avg of that column
satf = round(new_data['Saturated Fat'].mean(),1)
new_data['Saturated Fat'].fillna(satf, inplace=True)
#Saturated Fat


new_data.to_csv('burgerclean.csv',index=False)


df['Serving Size'].value_counts().plot.bar()
#sns.set(style="whitegrid", color_codes=True)
#ax1= sns.swarmplot(x="Category", y="Vitamin C (% Daily Value)", data=df)
print("\nketan")
#ax1.set_xticklabels(ax1.get_xticklabels(),rotation=90)
#ax1.plot()

