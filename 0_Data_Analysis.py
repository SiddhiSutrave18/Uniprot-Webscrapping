import pandas as pd

# <------------------------Write Input file name----------------------------------------------------->
df = pd.read_csv('Primary_data.csv').copy()
# <-------------------------------------------------------------------------------------------------->

organism_counts = df['Organism'].value_counts()

# Filter the DataFrame to keep only entries with organism names repeating more than once
df = df[df['Organism'].isin(organism_counts[organism_counts > 1].index)]

# Filter the entries which contain 'ec' in their Protein Names
df = df[~df['Protein names'].str.contains('EC')]

# Lower the capital letters for further analysis

df['Protein names'].apply(lambda x: x.lower())

# Give the keywords which has to be searched for filtration of protein names seperated with "|" as:
keyword = 'mlac|abc|phopholipid|toluene|tt2g|ttg2d|hpnm'
df = df[df['Protein names'].str.contains(keyword)]

# <------------------------Write Input file name----------------------------------------------------->
df.to_csv('WithoutUnrelated.csv')
# <-------------------------------------------------------------------------------------------------->

# Separate the entries into a list and give a relevant name to the listing file:
df['Entry'].to_csv('Strain_Search_List.csv')
