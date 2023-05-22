import pandas as pd
import numpy as np
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

# read database file
data = pd.read_csv('database.csv')

# fill nan with 0
data = data.fillna(0)

# return job level 
def get_level(string):
    if string == '1%2C2':
        level = 'Estágiario/Assistente'
    elif string == '4':
        level = 'Pleno/Senior'
    else:
        level = ''
    return level

# return job type
def get_type(string):
    if string == '1%2C3':
        type = 'Presencial/Hibrído'
    elif string == '2':
        type = 'Remoto'
    else:
        type = ''
    return type

# select the top n skills of a job search
def top_n_skills(row_index,n=10, type=None):
    # pick a subset from the database
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
    
    # description
    extra_info = [data.iloc[row_index][4],data.iloc[row_index][5],data.iloc[row_index][6]] # [type, level, number of job openings]
    space = 0
    if extra_info[1] != 0:
        type = get_type(extra_info[1])
        plt.text(n//2, max(plot['Percentage']), f"{type}", ha='center', fontsize=12)
        space += 2
    if extra_info[0] != 0:
        level = get_level(extra_info[0])
        plt.text(n//2, max(plot['Percentage']) - space, f"{level}", ha='center', fontsize=12)
        space += 2
    plt.text(n//2, max(plot['Percentage']) - space, f"n de vagas: {extra_info[2]}", ha='center', fontsize=12)

    # Bar chart showing how many times each term appears in job search results
    sns.barplot(x='column', y='Percentage', data=plot_1)

    # Add label for axis
    plt.xlabel(text)
    plt.ylabel("Porcentagem")
    
    # can use plt.savefig(f"{key}.png") to save corrent plot
    plt.show()

# Generate a plot showing the top n deltas of terms (requires two rows in the database at least)
def compare(row1, row2, n = 10, type = None):
    # pick a subset from the database
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
    
    # select rows
    job_data = job_data.iloc[[row1,row2]]
    
    # Transpose the DataFrame to get the columns on the x-axis
    job_datat = job_data.T
    
    # Rename the columns to 'value' for use in the bar plot
    job_datat.columns = ['value1', 'value2']
    
    # Reset the index so that the column names become a column of the DataFrame
    job_datat = job_datat.reset_index()
    
    # Convert Count values to percentages
    total1 = int(data.iloc[row1][6])
    job_datat['Percentage1'] = job_datat['value1'].apply(lambda x: (x / total1) * 100)
    total2 = int(data.iloc[row2][6])
    job_datat['Percentage2'] = job_datat['value2'].apply(lambda x: (x / total2) * 100)
    
    # Compare and mod columns
    job_datat['compare'] = job_datat['Percentage1'] - job_datat['Percentage2']
    job_datat['mod'] = abs(job_datat['compare'])
    
    # Rename the 'index' column to 'column'
    job_datat = job_datat.rename(columns={'index': 'column'})
    
    # Sort and pick the top n rows
    plot1 = job_datat.sort_values('mod', ascending=False)
    plot = plot1.head(n)
    
    # Set the width and height of the figure
    plt.figure(figsize=(10,6))

    # Add title
    key1 = data.iloc[row1][0]
    key2 = data.iloc[row2][0]
    plt.title(f"Diferença de requerimentos entre {key1} e {key2} ({text})")
    
    # description
    extra_info1 = [data.iloc[row1][4],data.iloc[row1][5],data.iloc[row1][6]] # [type, level, number of job openings]
    space = 0
    if extra_info1[1] != 0:
        type = get_type(extra_info1[1])
        plt.text(n - 2, max(plot['compare']), f"{type}", ha='center', fontsize=12)
        space += 2
    elif extra_info1[0] != 0:
        level = get_level(extra_info1[0])
        plt.text(n - 2, max(plot['compare']) - space, f"{level}", ha='center', fontsize=12)
        space += 2
    plt.text(n - 2, max(plot['compare']) - space, f"n de vagas: {extra_info1[2]}", ha='center', fontsize=12)
    
    extra_info2 = [data.iloc[row2][4],data.iloc[row2][5],data.iloc[row2][6]] # [type, level, number of job openings]
    if extra_info2[1] != 0:
        space += 2
        type = get_type(extra_info2[1])
        plt.text(n - 2, max(plot['compare']) - space, f"{type}", ha='center', fontsize=12)
    elif extra_info2[0] != 0:
        space += 2
        level = get_level(extra_info2[0])
        plt.text(n - 2, max(plot['compare']) - space, f"{level}", ha='center', fontsize=12)
    plt.text(n - 2, max(plot['compare']) - space - 2, f"n de vagas: {extra_info2[2]}", ha='center', fontsize=12)
    
    # Bar chart showing how many times each skill appears in job search results
    sns.barplot(x='column', y='compare', data=plot)

    # Add label for axis
    plt.xlabel(text)
    plt.ylabel("Porcentagem")
    
    # can use plt.savefig(f"{key}.png") to save corrent plot
    plt.show()
