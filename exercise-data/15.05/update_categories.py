import pandas as pd

dogs=pd.read_csv("ShelterDogs.csv")

# Change dtype as category
dogs['likes_children'] = dogs['likes_children'].astype('category')

# Create the my_changes dictionary
my_changes={"Maybe?" : "Maybe"}

# Rename the categories listed in the my_changes dictionary
dogs["likes_children"] = dogs["likes_children"].cat.rename_categories(my_changes)

# Use a lambda function to convert all categories to uppercase using upper()
dogs["likes_children"] =  dogs["likes_children"].cat.rename_categories(lambda c: c.upper())

# Print the list of categories
print(dogs["likes_children"].cat.categories)

##### Create the update_coats dictionary
update_coats={"wirehaired": "medium", "medium-long": "medium"}

# Create a new column, coat_collapsed
dogs["coat_collapsed"] =  dogs["coat"].replace(update_coats)

# Convert the column to categorical
dogs["coat_collapsed"] = dogs["coat_collapsed"].astype("category")

# Print the frequency table
print(dogs["coat_collapsed"].value_counts())

####
# Print out the current categories of the size variable
dogs["size"]=dogs["size"].astype("category")
print(dogs["size"].cat.categories)

# Reorder the categories, specifying the Series is ordinal, and overwriting the original series
dogs["size"].cat.reorder_categories(
  new_categories=["small", "medium", "large"],
  ordered=True,
  inplace=True
)

# How many Male/Female dogs are available of each size?
print(dogs.groupby(by=['size'])['sex'].value_counts())

# Do larger dogs need more room to roam?
print(dogs.groupby(by=["size"])["keep_in"].value_counts())

####
# Fix the misspelled word
replace_map = {"Malez": "male"}

# Update the sex column using the created map
dogs["sex"] = dogs["sex"].replace(replace_map)

# Strip away leading whitespace
dogs["sex"] = dogs["sex"].str.strip()

# Make all responses lowercase
dogs["sex"] = dogs["sex"].str.lower()

# Convert to a categorical Series
dogs["sex"] = dogs["sex"].astype("category")

print(dogs["sex"].value_counts())

####
# Print the category of the coat for ID 23807
print(dogs.loc[23807, "coat"])

# Find the count of male and female dogs who have a "long" coat
print(dogs.loc[dogs["coat"]=="long","sex"].value_counts())

# Print the mean age of dogs with a breed of "English Cocker Spaniel"
print(dogs.loc[dogs["breed"]=="English Cocker Spaniel", "age"].mean())

# Count the number of dogs that have "English" in their breed name
print(dogs[dogs["breed"].str.contains("English", regex=False)].shape[0])