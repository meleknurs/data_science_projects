import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes=pd.read_csv("crimes.csv")

# Which hour has the highest frequency of crimes? Store as an integer variable called peak_crime_hour.
crimes['hour']= crimes['TIME OCC'].str[:2].astype(int)
peak_crime_hour=crimes['hour'].value_counts().index[0]

# Which area has the largest frequency of night crimes (crimes committed between 10pm and 3:59am)? 
night_crimes=crimes[(crimes['hour'] >= 22) | (crimes['hour'] < 4)]
peak_night_crime_location=night_crimes['AREA NAME'].value_counts().index[0]

# Identify the number of crimes committed against victims by age group (0-17, 18-25, 26-34, 35-44, 45-54, 55-64, 65+)
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]

# Add a new column using pd.cut() to bin values into discrete intervals
crimes["Age Bracket"] = pd.cut(crimes["Vict Age"],
                               bins=age_bins,
                               labels=age_labels)

# Find the category with the largest frequency
victim_ages = crimes["Age Bracket"].value_counts()


print(victim_ages)