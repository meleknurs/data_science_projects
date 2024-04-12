import pandas as pd
from scipy import stats

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

#	Task 8: Calculate the mean, median, mode, skewness, variance and standard deviation of Price for all properties, no matter if sold or not.											

price=data['Price'].to_list()

mean = sum(price) / len(price)
median=price.median()
mode=price.mode()
skewness= price.skew()
variance=price.var()
std_dev=price.std()

print("Mean Price:", mean)
print("Median Price:", median)
print("Mode Price:", mode)
print("Skewness of Price:", skewness)
print("Variance of Price:", variance)
print("Standard Deviation of Price:", std_dev)