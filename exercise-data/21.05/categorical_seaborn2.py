import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
reviews = pd.read_csv("lasvegas_tripadvisor.csv")

# Set the font size to 1.25
sns.set(font_scale=1.25)

# Set the background to "darkgrid"
sns.set_style("darkgrid")

# Create a scatter plot
sns.scatterplot(
    x="Helpful votes",
    y="Score",
    hue="Traveler type",
    data=reviews
)

plt.title("Score vs. Helpful Votes by Traveler Type")
plt.show()
