import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

# Task 5: Create a scatter plot showing the relationship between Price and Area. 

price=data['Price'].to_list()

area= data['Area (ft.)'].to_list()

# create scatter plot
plt.scatter(area, price, alpha=0.5)
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Scatter Plot of Price vs Area")
#plt.show()

# Task 6: Create a frequency distribution table, where you list all the countries from which the company has buyers (country vs number of buyers). 
# Count the absolute frequency, the relative frequency and the cumulative frequency. 																	
country = data['Country'].dropna()

frequency_table = country.value_counts().reset_index()
frequency_table.columns = ["Country", "Absolute Frequency"]

total_buyers = len(country)
frequency_table['Relative Frequency'] = frequency_table["Absolute Frequency"] / total_buyers
frequency_table['Cumulative Frequency'] = frequency_table['Relative Frequency'].cumsum()

print(frequency_table[['Country', 'Cumulative Frequency']])



