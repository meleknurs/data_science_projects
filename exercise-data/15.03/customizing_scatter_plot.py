import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

mpg= pd.read_csv("mpg.csv")


# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue= "cylinders")

# Show plot
plt.show()

# Create a scatter plot of acceleration vs. mpg
sns.relplot(x= "acceleration",
            y= "mpg",
            data=mpg,
            kind= "scatter",
            style= "origin",
            hue= "origin")



# Show plot
plt.show()