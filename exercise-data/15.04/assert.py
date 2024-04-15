import pandas as pd


df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Check that column 'C' exists in the DataFrame
assert 'C' in df.columns, "Column 'C' is missing"

# Check that all values in column 'A' are greater than 0
assert (df['A'] > 0).all(), "Values in column 'A' must be greater than 0"
