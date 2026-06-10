import pandas as pd 
import numpy as np

# Load the dataset
df = pd.read_csv("Heart_Disease_Prediction.csv")
print(df.head(10))
print("-" * 100 )


#Check the missing values

print(df.isnull().sum())  #No missing value we find
print("-" * 100 )

#Check shape and columns 

print("Shape : " , df.shape)  # (270 , 14)
print("-" * 100 )
print(df.columns)
print("-" * 100 )


#Info 
print(df.info())


#Changing one that column which is present in float to integer
df["ST depression"] = df["ST depression"].astype(int)
print("-" * 100 )

#saving the cleaned dataset
df.to_csv("Heart_Disease_Prediction_cleandataset.csv")
print("CSV file saved successfully.")