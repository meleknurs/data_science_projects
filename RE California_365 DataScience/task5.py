import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

# Task 3: Create a histogram which represents the Price variable. Choose interval width (bins) of length $100,000. 

price=data['Price'].to_list()

#calculate number of bins
bin_width = 100000
num_bins = int((max(price) - min(price)) / bin_width)
print(num_bins)

#create an histogram
plt.hist(price, bins=num_bins)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Frequency of Distribution")
plt.show()