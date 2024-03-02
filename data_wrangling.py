import pandas as pd
import os

# Set the current working directory
os.chdir('C:/Users/malec/OneDrive/Analýzy/Data science')

# Input file path
input_file = 'source/job_skills.csv'

# Read data from input CSV with the specified delimiter and quote character
df = pd.read_csv(input_file, delimiter=',', quotechar='"', engine='python', nrows=5)


df['ID'] = df['job_link'].str.split('-').str[-1]
df['job_name'] = df['job_link'].str.extract(r'/([^/]+)-at')
df['job_name'] = df['job_name'].str.replace('-', ' ')
df['company_name'] = df['job_link'].str.extract(r'-at-([\w\s-]+)-\d+$')
df['company_name'] = df['company_name'].str.replace('-', ' ')

df_skills_split = df['job_skills'].str.split(',', expand=True)

# Merge the split columns back with the original dataframe
columns = ['ID', 'job_link', 'job_name', 'company_name']

df_merged = pd.concat([df[columns], df_skills_split], axis=1)

df_melt = pd.melt(df_merged, id_vars=columns, value_vars=df_skills_split).dropna()
df_fact = df_melt[['ID', 'value']]
df_dim = df[columns]

rewrite = True

if rewrite == True:
    output_fact_file = 'output/output_data_fact.xlsx'
    df_fact.to_excel(output_fact_file, index=True)  # Set index=False to exclude row numbers
    print(f"DataFrame written to {output_fact_file}")
    output_dim_file = 'output/output_data_dim.xlsx'
    df_dim.to_excel(output_dim_file, index=False)
    print(f"DataFrame written to {output_dim_file}")
else:
    print(df_melt)
    print(df_dim)
    print(df_fact)

