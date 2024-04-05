import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

men_results=pd.read_csv("men_results.csv")
women_results=pd.read_csv("women_results.csv")

# use data since '2002-01-01' and only for FIFA World Cup tournaments
filtered_men_data = men_results[men_results['date']>= '2002-01-01']
filtered_men_data= filtered_men_data[filtered_men_data['tournament'] == 'FIFA World Cup']

filtered_women_data=women_results[women_results['date'] >= '2002-01-01']
filtered_women_data=filtered_women_data[filtered_women_data['tournament']=='FIFA World Cup']


#filter 'date','home_score','away_score' columns
men_data=filtered_men_data[['date','home_score','away_score']]
women_data=filtered_women_data[['date','home_score','away_score']]





'''p_val=

result= ["fail to reject","reject"]
result_dict = {"p_val": p_val, "result": result}'''