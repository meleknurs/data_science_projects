import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("re_california.xlsx", sheet_name= "365RE", skiprows=4)

print(data.columns) 