import csv
import pandas as pd
from searchdata import info as data
# Define a list of words to count
words_to_count = ["python", "SQL", "Pacote Office", "Power BI", "SQLite", "Git", "Java", "AWS", "Pandas"]

def count_words_in_csv(csv_filename, words_to_count):
    # Open the CSV file for reading
    with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        # Initialize a set to keep track of words that have already been counted
        words_already_counted = set()

        # Initialize a dictionary to store the word counts
        word_counts = {word: 0 for word in words_to_count}

        # Iterate over each row in the CSV file
        for row in reader:
            # Iterate over each cell in the row
            for cell in row:
                # Check if the cell contains any of the words to count
                for word in words_to_count:
                    if word.lower() in cell.lower() and word not in words_already_counted:
                        word_counts[word] += 1
                        words_already_counted.add(word)

            # Reset the set of words already counted for the next row
            words_already_counted = set()
        # add how many discriptions were used
        csv_file.seek(0)
        word_counts['Total jobs'] = sum(1 for row in reader)
    # Return the word counts
    return word_counts


word_counts = count_words_in_csv('job_descriptions.csv', words_to_count)
# make a new csv file with the clean data
columns = data.copy()
columns.update(word_counts)
database = pd.DataFrame(columns,index=[0])
database.to_csv('database.csv')
print(database)