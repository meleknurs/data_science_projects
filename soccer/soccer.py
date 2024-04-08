import pandas as pd
import numpy as np
from scipy.stats import norm


men_results = pd.read_csv("men_results.csv")
women_results = pd.read_csv("women_results.csv")

# Filter data for FIFA World Cup tournaments since '2002-01-01'
filtered_men_data = men_results[(men_results['date'] >= '2002-01-01') & (men_results['tournament'] == 'FIFA World Cup')]
filtered_women_data = women_results[(women_results['date'] >= '2002-01-01') & (women_results['tournament'] == 'FIFA World Cup')]

# Select relevant columns
men_data = filtered_men_data[['date', 'home_score', 'away_score']]
women_data = filtered_women_data[['date', 'home_score', 'away_score']]

# Calculate total goals and mean for men's data
men_data['total_goals'] = men_data['home_score'] + men_data['away_score']
men_mean = men_data['total_goals'].mean()

# Calculate total goals and mean for women's data
women_data['total_goals'] = women_data['home_score'] + women_data['away_score']
women_mean = women_data['total_goals'].mean()

# Calculate standard deviations for men's and women's data
men_std = men_data['total_goals'].std()
women_std = women_data['total_goals'].std()

# Calculate standard error
standard_error = ((men_std ** 2) / men_data.shape[0] + (women_std ** 2) / women_data.shape[0]) ** 0.5

# Calculate z-score
z_score = (women_mean - men_mean) / standard_error

# Calculate p-value
p_val = norm.cdf(z_score)

# Determine result based on p-value
result_categories = ["fail to reject", "reject"]
result = result_categories[int(p_val <= 0.10)]  # Assuming significance level of 0.10

# Create result dictionary
result_dict = {"p_val": p_val, "result": result}

print(result_dict)
