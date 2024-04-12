import streamlit as st

# Title of the dashboard
st.title('My Streamlit Dashboard')

# Add some text or markdown
st.write('Here you can add some text.')

# Create a sidebar for additional options
st.sidebar.write('Sidebar')

# Add interactive widgets like sliders, buttons, etc.
user_input = st.text_input('Enter your name', 'Type here...')
st.write('Hello, ', user_input, '!')

# Display data in tables or charts
import pandas as pd
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': [10, 20, 30, 40]
})
st.write('A simple DataFrame:')
st.write(df)
