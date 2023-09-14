import pandas as pd

# Read the 'seminar' sheet from the Excel file
df = pd.read_excel('parsed.xlsx', sheet_name='seminar')

# Remove duplicate (stu_id, seminar) pairs
df_unique = df.drop_duplicates(subset=['stu_id', 'seminar'])

# Count frequencies of each unique seminar
seminar_counts = df_unique['seminar'].value_counts().reset_index()
seminar_counts.columns = ['seminar', 'frequency']

# Print out the frequency distribution
print(seminar_counts)

# Optionally, write the frequency distribution to a new Excel file
seminar_counts.to_excel('seminar_frequencies.xlsx', index=False)
