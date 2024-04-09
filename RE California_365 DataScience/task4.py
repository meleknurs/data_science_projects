import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

#Task 2: Create a frequency distribution graph representing the price (that is a histogram with the highest possible number of bins - 267). 

price=data['Price'].to_list()

#calculate bin width
num_bins= 267
price_range=max(price)- min(price)
bin_width= price_range/num_bins

#create bins
bins= np.arange(min(price), max(price)+ bin_width, bin_width)

#calculate frequencies
hist, _ = np.histogram(price, bins=bins)

#create an histogram
plt.hist(price, bins=num_bins)
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Prices')
plt.show()


