import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

student_data= pd.read_csv("student-alcohol-consumption.csv")

# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
#plt.show()


##########

# Create a scatter plot of G1 vs. G3
sns.relplot(x= "G1", y= "G3",
             data= student_data,
             kind= "scatter",
             )


# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            row="famsup",
            row_order=["yes", "no"],
            col_order=["yes", "no"])

# Show plot
plt.show()