import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

reviews= pd.read_csv("lasvegas_tripadvisor.csv")

# Set the font size to 1.25
sns.set(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style("darkgrid")

# Create a boxplot
sns.catplot(
    x="Traveler type",
    y="Helpful votes",
    data= reviews,
    kind="box"
)

plt.show()

####
# Create a bar chart
sns.set_theme(font_scale=.9)
sns.set_style("whitegrid")
sns.catplot(x="User continent", y= "Score", data=reviews, kind="bar")
plt.show()

# Set style
sns.set_theme(font_scale=.9)
sns.set_style("whitegrid")

# Print the frequency counts for "User continent"
print(reviews["User continent"].value_counts())

# Convert "User continent" to a categorical variable
reviews["User continent"] = reviews["User continent"].astype("category")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()

# Reorder "User continent" using continent_categories and rerun the graphic
continent_categories = list(reviews["User continent"].value_counts().index)
reviews["User continent"] = reviews["User continent"].cat.reorder_categories(new_categories=continent_categories)
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar")
plt.show()

######
# Add a second category to split the data on: "Free internet"
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="Casino", y="Score", data=reviews, kind="bar", hue="Free internet")
plt.show()

# Switch the x and hue categories
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="Free internet", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

# Update x to be "User continent"
sns.set_theme(font_scale=2)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()

# Lower the font size so that all text fits on the screen.
sns.set_theme(font_scale= 1)
sns.set_style("darkgrid")
sns.catplot(x="User continent", y="Score", data=reviews, kind="bar", hue="Casino")
plt.show()