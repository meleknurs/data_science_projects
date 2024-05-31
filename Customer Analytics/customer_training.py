# Import necessary libraries
import pandas as pd

# Load the dataset
ds_jobs = pd.read_csv("customer_train.csv")

# View the dataset
ds_jobs.head()


# Create a copy of ds_jobs for transforming
ds_jobs_transformed = ds_jobs.copy()

# Check the data types of the columns
print(ds_jobs.info())

# Identify ordinal, nominal, and two-factor categories
for column in ds_jobs.select_dtypes("object").columns:
    print('column_name:', column, '\n', ds_jobs_transformed[column].value_counts(), '\n')
   
# Create a dictionary for ordered categorical data
ordered_cats= {
    'enrolled_university' : ['no_enrollment', 'Part time course', 'Full time course'],
    'education_level': ['Primary School', 'High School', 'Graduate', 'Masters', 'Phd'],
    'experience' :  ['<1'] + list(map(str, range(1, 21))) + ['>20'],
    'company_size': ['<10', '10-49', '50-99', '100-499', '500-999', '1000-4999', '5000-9999', '10000+'],
    'last_new_job': ['never', '1', '2', '3', '4', '>4']
}

# Create a map for containing 2-factor categories to convert bool
two_factor_cats = { 
    'relevant_experience': {'No relevant experience': False, 'Has relevant experience' : True},
    'job_change' : {0.0: False, 1.0: True}
}

# Create a loop to change data type
for col in ds_jobs_transformed:
    
    # Convert two-factor categories to bool
    if col in ['relevant_experience', 'job_change']:
        ds_jobs_transformed[col] = ds_jobs_transformed[col].map(two_factor_cats[col])
        
    # Convert int64 to int32
    elif col in ['student_id', 'training_hours']:
        ds_jobs_transformed[col]= ds_jobs_transformed[col].astype("int32")
        
    # Convert float to float16
    elif col in ['city_development_index']:
        ds_jobs_transformed[col]= ds_jobs_transformed[col].astype("float16")
        
    # Convert columns in ordered categorical data
    elif col in ordered_cats.keys():
        category = pd.CategoricalDtype(ordered_cats[col], ordered=True)
        ds_jobs_transformed[col]= ds_jobs_transformed[col].astype(category)
        
    else:
        ds_jobs_transformed[col]= ds_jobs_transformed[col].astype("category")

# Filter students with 10 or more years of experience at companies with at least 1000 employees     
ds_jobs_transformed = ds_jobs_transformed[(ds_jobs_transformed['experience'] >= '10') & (ds_jobs_transformed['company_size'] >= '1000-4999')]