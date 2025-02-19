import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a title and subtitle
st.title('News Correlation Dashboard')

# Define the file paths
file_path = 'data/cleaned_data.csv'
file_path2 = 'C:\\Users\\gecha\\OneDrive\\Documents\\news_correlation_10ac_week0\\Data\\domains_location.csv'
file_path2 = file_path2.replace("\\", "/")

# Load the cleaned data into a DataFrame
cleaned_df = pd.read_csv(file_path)
location_df = pd.read_csv(file_path2)

# Perform a count of news articles by source
source_counts = cleaned_df['source_name'].value_counts()

# Get the top 10 sources with the largest count of news articles
top_10_sources = source_counts.head(10)

# Plot the bar chart for top 10 websites
fig, ax = plt.subplots()
top_10_sources.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Top 10 Websites with the Largest Count of News Articles')
ax.set_xlabel('Website')
ax.set_ylabel('Number of Articles')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Count occurrences of each country
country_counts = location_df['Country'].value_counts()

# Get the top 10 countries with the most articles written
top_10_countries = country_counts.head(10)

# Plot the bar chart for top 10 countries
fig, ax = plt.subplots()
top_10_countries.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Top 10 Countries with media organizations')
ax.set_xlabel('Country')
ax.set_ylabel('Number of media')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

st.subheader("Media List")

file_path2 = 'C:\\Users\\gecha\\OneDrive\\Documents\\news_correlation_10ac_week0\\Data\\domains_location.csv'
file_path2 = file_path2.replace("\\", "/")
location_df = pd.read_csv(file_path2)

location_df



# Create some sample data (replace with your cleaned data)
data = {'source_name': ['Reuters', 'BBC News', 'CNN', 'New York Times', 'Reuters', 'BBC News', 'CNN', 'Fox News']}
df = pd.DataFrame(data)

# Perform a count of news articles by source
source_counts = df['source_name'].value_counts()

# Get the source with the largest count of news articles
largest_source = source_counts.idxmax()
largest_count = source_counts.max()


# Display top 10 sources
st.subheader("Top 10 Websites with Most Articles")
st.dataframe(top_10_sources)

# You can add charts here as well using libraries like matplotlib or plotly
# st.bar_chart(top_10_sources)  # Example bar chart of top 10 sources
