# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Ensure the file path is correct or the file exists in the current directory
# Example: df = pd.read_csv("/path/to/nobel.csv") if the file is not in the current directory
df = pd.read_csv("nobel.csv")  # Assuming the file is now in the correct location or path is corrected

print(df.columns)

# What is the most commonly awarded gender and birth country?
top_gender = df["sex"].value_counts(ascending=False).index[0]
top_country= df["birth_country"].value_counts(ascending=False).index[0]

print(top_gender)
print(top_country)

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
us_born_winners= df[df['birth_country'] == 'United States of America'].dropna()
us_born_winners['decade']= (us_born_winners['year'] // 10) * 10
max_decade_usa= us_born_winners['decade'].value_counts().index[0]
print(max_decade_usa)

# Who was the first woman to receive a Nobel Prize, and in what category?
woman_winners_index= df[df['sex']== 'Female'].index[0]
first_woman_name= df.iloc[woman_winners_index]['full_name']
first_woman_category= df.iloc[woman_winners_index]['category']

# Which individuals or organizations have won more than one Nobel Prize throughout the years?
repeat_list=df['organization_name'].value_counts().index[0]
