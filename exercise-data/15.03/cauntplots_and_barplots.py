import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

survey_data=pd.read_csv("young-people-survey-responses.csv")

# Create count plot of internet usage
sns.catplot(x="Internet usage",
                data=survey_data,
                kind="count")

# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col= "Age category")

# Show plot
plt.show()

######
# Create a bar plot of interest in math, separated by gender
sns.catplot(x="Gender", y= "Interested in Math",
            data= survey_data, kind="bar")

#####
# Create bar plot of average final grade in each study category
sns.catplot(x="study_time", y="G3", data= student_data, kind= "bar")

# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            )

# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar",
            order=category_order,
            ci=None)

plt.show()

#####
# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories
sns.catplot(x="study_time", y= "G3", data= student_data, kind="box", order=study_time_order)

# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", data=student_data, kind= "box", col="location", sym="", hue="location")

###
# Set the whiskers to 0.5 * IQR
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=0.5)

# Extend the whiskers to the 5th and 95th percentile
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[5,95])

# Set the whiskers at the min and max values
sns.catplot(x="romantic", y="G3",
            data=student_data,
            kind="box",
            whis=[0, 100])


######
# Create a point plot of family relationship vs. absences
sns.catplot(x="famrel", y="absences", data= student_data,kind= "point")

# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2)

# Remove the lines joining the points
sns.catplot(x="famrel", y="absences",
			data=student_data,
            kind="point",
            capsize=0.2,
            join=False)

####
# Create a point plot that uses color to create subgroups
sns.catplot(x= "romantic", y="absences", data=student_data, kind="point", hue="school")

# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None)

# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences",
			data=student_data,
            kind="point",
            hue="school",
            ci=None,
            estimator= median)

# Set the style to "whitegrid"
sns.set_style("whitegrid")

# Create a count plot of survey responses
category_order = ["Never", "Rarely", "Sometimes", 
                  "Often", "Always"]

sns.catplot(x="Parents Advice", 
            data=survey_data, 
            kind="count", 
            order=category_order)

# Set the color palette to "Purples"
sns.set_style("whitegrid")
sns.set_palette("Purples")

# Set the context to "paper"
sns.set_context("paper")

# Create bar plot
sns.catplot(x="Number of Siblings", y="Feels Lonely",
            data=survey_data, kind="bar")

# Set the style to "darkgrid"
sns.set_style("darkgrid")

# Set a custom color palette
sns.set_palette(["#39A7D0","#36ADA4"])

# Show plot
plt.show()


