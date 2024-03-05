import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


food_consumption = pd.read_csv("food_consumption.csv")

print(food_consumption.head())

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']


# Calculate mean and median consumption in Belgium
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))



# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption["country"] == 'Belgium') | (food_consumption["country"] == 'USA')]


# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean,np.median]))



# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']



# Histogram of co2_emission for rice and show plot
plt.hist(rice_consumption['co2_emission'])
plt.show()


# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']



# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg([np.mean, np.median]))

