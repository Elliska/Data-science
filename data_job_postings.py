import pandas as pd
import os

# Set the current working directory
os.chdir('C:/Users/malec/OneDrive/Analýzy/Data science')

# Input file path
input_file = 'source/job_postings.csv'

# Read data from input CSV with the specified delimiter and quote character
df = pd.read_csv(input_file, delimiter=',', quotechar='"', engine='python', nrows=5)

df['ID'] = df['job_link'].str.split('-').str[-1]
df['last_processed'] = df.to_date['last_processed_time']
columns = ['ID', 'job_link', 'last_processed_time', 'job_title', 'company', 'job_location', 'first_seen', 'search_city', 'search_country', 'search_position', 'job_level', 'job_type']

df = df[columns]


rewrite = True

if rewrite == True:
    output_fact_file = 'output/output_job_postings.xlsx'
    df.to_excel(output_fact_file, index=False)  # Set index=False to exclude row numbers
    print(f"DataFrame written to {output_fact_file}")
else:
    print(df)

