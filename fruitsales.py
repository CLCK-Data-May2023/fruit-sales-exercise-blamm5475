import pandas as pd

# Create the DataFrame
data = {'Apples': [35, 41],
        'Bananas': [21, 34]}

index = ['2017 Sales', '2018 Sales']

df = pd.DataFrame(data, index=index)

# Write the DataFrame to a CSV file
df.to_csv('fruit.csv')
