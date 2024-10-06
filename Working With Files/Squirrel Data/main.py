import pandas
from pandas.core.interchange.dataframe_protocol import DataFrame

data = pandas.read_csv("Squirrel_Census_2018.csv")
# Select the desired column
column_name = 'Primary Fur Color'

# Get unique, non-null values and their counts
unique_values = data[column_name].dropna().value_counts()

# Print or store the result
print(unique_values)
df = pandas.DataFrame(unique_values)
df.to_csv("squirrel_count.csv")


