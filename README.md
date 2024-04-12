# news_correlation_10ac_week0



# Project Name

## Description
This project involves analyzing news articles and sentiment data using Python and PostgreSQL.

## Tasks Completed
1. Identified the countries with the most news coverage and extracted the top countries mentioned in the news content.
2. Analyzed the sentiment of news articles and compared the impact of using mean/average and median for sentiment analysis.
3. Pushed data from a pandas DataFrame to a PostgreSQL database.
4. Created a table in the PostgreSQL database to store the analyzed data.

## Code Examples
### Identifying Top Countries in News Content
```python
# Python code for identifying top countries mentioned in news content
import pandas as pd
import re

# Assuming you have the data in a DataFrame called df and the country list in a DataFrame called country_df with a column named "Country"
# Replace df and country_df with the actual names of your DataFrames if they're different

# Convert the "Country" column to strings to handle any float values
location_df['Country'] = location_df['Country'].astype(str)

# Read the country list from the "Country" column of the other table
country_list = location_df['Country'].tolist()

# Create a regular expression pattern to match the countries of interest
country_pattern = r'\b(?:' + '|'.join(country_list) + r')\b'

# Apply the regular expression pattern to the content column to identify articles about the countries of interest
cleaned_df['country_mentioned'] = cleaned_df['content'].str.contains(country_pattern, flags=re.IGNORECASE, na=False)

# Count the occurrences of articles mentioning each country
country_counts = cleaned_df['country_mentioned'].sum()
```

### Pushing Data to PostgreSQL Database
```python
# Python code for pushing data to a PostgreSQL database
import pandas as pd
from sqlalchemy import create_engine

# Assuming you have a DataFrame called df and a PostgreSQL database connection string
# Replace 'your_connection_string' with your actual connection string
connection_string = 'postgresql://username:password@host:port/database_name'

# Create a database connection
engine = create_engine(connection_string)

# Push the data from the DataFrame to the PostgreSQL database
df.to_sql('table_name', engine, if_exists='replace', index=False)
```

## Author
Getachew Abebe