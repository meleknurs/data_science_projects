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
#plt.show()


# Create line plot
sns.relplot(x="model_year",
            y= "mpg",
            data= mpg,
            kind= "line")


# Show plot
plt.show()

######
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line",
            ci="sd")

# Show plot
plt.show()


# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin",
            markers= True,
            dashes=False)

# Show plot
plt.show()