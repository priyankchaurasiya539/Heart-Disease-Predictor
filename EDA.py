import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#Load the new dataset
df = pd.read_csv("data/Heart_Disease_Prediction_cleandataset.csv")
print(df.head(10))


"""Visualization"""

#Graph - how many males and females have heart disease

counts = df.groupby(["Sex" , "Heart Disease"]).size().unstack()
counts.plot(kind="bar" , figsize=(8 , 6) , edgecolor = "black")
plt.title("Number of Males & Females who have and have not Heart Disease")
plt.xlabel("Males & Females")
plt.ylabel("Number of Persons")
plt.xticks( [0, 1] , ["Females" , "Males"] , rotation = 0 )
plt.savefig("Graphs(EDA)/Distribution of people have disease.png")
plt.show()

#Graph - how many males and females have Max HR score

plt.figure(figsize=(8 , 6))
df.boxplot(column = "Max HR" , by="Sex" )
plt.title("Number of Males and females have Max HR")
plt.xlabel("Males & Females")
plt.ylabel("Max HR")
plt.xticks([1 , 2] , ["Females" , "Males"] , rotation = 0 )     #Why here [1 , 2 ] because when we use boxplot , in this python starts it index from 1 so that's why here [1 , 2 ]....
plt.savefig("Graphs(EDA)/MaxHR.png")
plt.show()


#Graph between the Chest pain type and sex
count_chest_pain = df.groupby(["Sex" , "Chest pain type"]).size().unstack()
count_chest_pain.plot(kind="bar" , figsize=(8 , 6) , color = ["cyan", "skyblue" , "lightcoral" , "teal"] , edgecolor = "black")
plt.title("Chest Pain type with people category")
plt.xlabel("Chest pain type")
plt.ylabel("Number of Persons")
plt.xticks([0 , 1 ] , ["Females" , "Males"] , rotation = 0 )
plt.savefig("Graphs(EDA)/Chest Pain type with number of persons.png")
plt.show()