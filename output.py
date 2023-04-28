import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# read database file
data = pd.read_csv('database.csv')

#pick the skills from the database
job_data = data.iloc[:, 7:]

# Transpose the DataFrame to get the columns on the x-axis
job_datat = job_data.T

# Rename the columns to 'value' for use in the bar plot
job_datat.columns = ['value']

# Reset the index so that the column names become a column of the DataFrame
job_datat = job_datat.reset_index()

# Rename the 'index' column to 'column'
job_datat = job_datat.rename(columns={'index': 'column'})

# Set the width and height of the figure
plt.figure(figsize=(10,6))

# Add title
key = data['keywords'][0]
plt.title(f"Requisitos para {key}")

# Bar chart showing how many times each skill appears in job search results
sns.barplot(x='column', y='value', data=job_datat)

# Add label for axis
plt.xlabel("Skills")
plt.ylabel("number of times a skill appears in each job search results")
plt.show()