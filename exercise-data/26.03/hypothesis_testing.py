import pandas as pd
import numpy as np
from scipy.stats import norm

late_shipments=pd.read_feather("late_shipments.feather")

# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp = np.mean(late_shipments['late'] == 'Yes') 

# Print the results
print(late_prop_samp)

# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn, ddof=1)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) /std_error

# Print z_score
print(z_score)

###
# Calculate the z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Calculate the p-value
p_value = 1- norm.cdf(z_score,loc=0, scale=1)
                 
# Print the p-value
print(p_value) 
###

# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))