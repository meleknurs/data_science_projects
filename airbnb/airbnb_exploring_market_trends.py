# Import necessary packages
import pandas as pd
import numpy as np

# Load airbnb_price.csv type of data
airbnb_price= pd.read_csv("data/airbnb_price.csv")

# Check the csv data
print("\nCSV data:")
print(airbnb_price.head())

# Load airbnb_last_review.tsv type of data
airbnb_last_review= pd.read_csv("data/airbnb_last_review.tsv", sep="\t")

#Check the tsv data
print("\nTSV data:")
print(airbnb_last_review.head())

# Load airbnb_room_type.xlsx type of data
airbnb_room_type= pd.read_excel('data/airbnb_room_type.xlsx')

#Check the excell data
print("\nExcel data:")
print(airbnb_room_type.head())

# Merge the datas into one
merged_data= pd.merge(airbnb_price, airbnb_last_review, on='listing_id')
merged_data= pd.merge(merged_data, airbnb_room_type, on= 'listing_id')

# What are the dates of the earliest and most recent reviews? 
# Convert "last_review" column to datetime format
merged_data['last_review'] = pd.to_datetime(merged_data['last_review'], format='%B %d %Y')

# Find and print the earliest review
earliest_review=merged_data['last_review'].min()
print("\nEarliest review date:")
print(earliest_review)

#Find and print the latest review
latest_review=merged_data['last_review'].max()
print("\nLatest review date:")
print(latest_review)

#How many of the listings are private rooms?
# Clean the data with using str.lower() method
merged_data['room_type']=merged_data['room_type'].str.lower()
private_rooms= merged_data[merged_data['room_type']=='private room'].shape[0]
print('\nPrivate rooms:')
print(private_rooms)

#What is the average listing price? Round to the nearest two decimal places and save into a variable
# Clean the prce column with .str.replace() method
merged_data["price"]= merged_data['price'].str.replace('dollars', "")
#print(merged_data['price'].dtype)
merged_data["price"]= merged_data['price'].astype('float')
#print(merged_data['price'].dtype)
average_price= merged_data['price'].mean().round(2)
print("\nAverage price of the rooms:")
print(average_price)

#Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price
review_dates= pd.DataFrame({
   'first_reviewed': [earliest_review],
    'last_reviewed': [latest_review], 
    'nb_private_rooms': [private_rooms],
    'avg_price' : [average_price]
})

print(review_dates)