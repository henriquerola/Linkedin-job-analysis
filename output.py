import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# read database file
data = pd.read_csv('database.csv')

# select the top n skills of a job search
def top_n_skills(row_index,n, type=None):
    #pick the skills from the database
    if type is None or type == 'all':
        text = 'habilidades'
        job_data = data.iloc[:, 7:]
    elif type is None or type == 'programming language':
        text = 'linguagens de programação'
        job_data = data.iloc[:, 7:34]
    elif type is None or type == 'frameworks':
        text = 'frameworks'
        job_data = data.iloc[:, 34:58]
    elif type is None or type == 'databases':
        text = 'banco de dados'
        job_data = data.iloc[:, 58:84]
    elif type is None or type == 'libraries':
        text = 'bibliotecas'
        job_data = data.iloc[:, 84:100]
    elif type is None or type == 'cloud':
        text = 'nuvens'
        job_data = data.iloc[:, 100:125]
    elif type is None or type == 'tools':
        text = 'ferramentas'
        job_data = data.iloc[:, 125:157]
    else:
        quit()
        
    # select the row
    job_data = job_data.iloc[[row_index]]
    
    # Transpose the DataFrame to get the columns on the x-axis
    job_datat = job_data.T
    
    # Rename the columns to 'value' for use in the bar plot
    job_datat.columns = ['value']
    
    # Reset the index so that the column names become a column of the DataFrame
    job_datat = job_datat.reset_index()
    
    # Convert Count values to percentages
    total = int(data.iloc[row_index][6])
    job_datat['Percentage'] = job_datat['value'].apply(lambda x: (x / total) * 100)
    
    # Rename the 'index' column to 'column'
    job_datat = job_datat.rename(columns={'index': 'column'})
    plot = job_datat.sort_values('Percentage', ascending=False)
    plot_1 = plot.head(n)
    
    # Set the width and height of the figure
    plt.figure(figsize=(10,6))

    # Add title
    key = data.iloc[row_index][0]
    plt.title(f"Top {n} {text} mais requisitadas para {key}")

    # Bar chart showing how many times each skill appears in job search results
    sns.barplot(x='column', y='Percentage', data=plot_1)

    # Add label for axis
    plt.xlabel(text)
    plt.ylabel("Porcentagem")
    plt.show()
    
top_n_skills(0,10,'all')
top_n_skills(0,10,'tools')