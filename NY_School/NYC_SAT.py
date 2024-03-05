import pandas as pd
import numpy as np

schools = pd.read_csv("schools.csv")


print(schools.head())



# Best math results
min_math_score = 0.8 * 800
best_math_schools = schools[schools['average_math'] >= min_math_score]
best_math_schools = best_math_schools[['school_name', 'average_math']].sort_values(by='average_math', ascending=False)