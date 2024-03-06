import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")


print(schools.head())



# Best math results
min_math_score = 0.8 * 800
best_math_schools = schools[schools['average_math'] >= min_math_score]
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)

#  Top 10 performing schools
schools["total_SAT"]= schools["average_math"] + schools["average_reading"] +schools["average_writing"] 
top_10_schools= schools[["school_name", "total_SAT"]].sort_values(by='total_SAT', ascending= False).head(10)



# The largest standard deviation
borough_stats = schools.groupby('borough')['total_SAT'].agg(['size', 'mean', 'std']).round(2)
largest_std_dev_borough = borough_stats['std'].idxmax()
largest_std_dev = pd.DataFrame({
    'borough': [largest_std_dev_borough],
    'num_schools': [borough_stats.loc[largest_std_dev_borough, 'size']],
    'average_SAT': [borough_stats.loc[largest_std_dev_borough, 'mean']],
    'std_SAT': [borough_stats.loc[largest_std_dev_borough, 'std']]
})


print(largest_std_dev)