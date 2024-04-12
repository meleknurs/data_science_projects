import pandas as pd
from scipy import stats

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

#	Task 10: Calculate the covariance and correlation coefficient between Price and Area, no matter if the property is sold or not. Is the result in line with the scatter plot?
				
price=data['Price']
area= data['Area (ft.)']

covariance= price.cov(area)

correlation_coeff= price.corr(area)

print("Covariance between Price and Area:", covariance)
print("Correlation coefficient between Price and Area:", correlation_coeff)