import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

reviews= pd.read_csv("lasvegas_tripadvisor.csv")

# Create a point plot with catplot using "Hotel stars" and "Nr. reviews"
sns.catplot(
  # Split the data across Hotel stars and summarize Nr. reviews
  x="Hotel stars" ,
 y= "Nr. reviews",
  data=reviews,
  # Specify a point plot
  kind= 'point',
  hue="Pool",
  # Make sure the lines and points don't overlap
  dodge= True
)
plt.show()


####
sns.set_theme(font_scale=1.4)
sns.set_style("darkgrid")

# Create a catplot that will count the frequency of "Score" across "Traveler type"
sns.catplot(
  x="Score",
  data=reviews,
  kind="count",
  hue="Traveler type"
)

plt.show()