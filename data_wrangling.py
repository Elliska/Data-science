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

#df['company_name'] = df['job_link'].str.extract(r'at\s*([^\-]+)\s*-')
df['company_name'] = df['job_link'].str.extract(r'-at-(\w+)-\d+$')
df['company_name'] = df['company_name'].str.replace('-', ' ')

df_skills_split = df['job_skills'].str.split(',', expand=True)

# Merge the split columns back with the original dataframe
columns = ['ID', 'job_link', 'job_name', 'company_name']

df_merged = pd.concat([df[columns], df_skills_split], axis=1)

df_melt = pd.melt(df_merged, id_vars=columns, value_vars=df_skills_split).dropna()


rewrite = False

if rewrite == True:
    output_file = 'output_data.xlsx'
    df_melt.to_excel(output_file, index=False)  # Set index=False to exclude row numbers
    print(f"DataFrame written to {output_file}")
else:
    print(df_melt)
    #print(df_merged)7:

