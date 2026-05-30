import pandas as pd



#------------------------ SERIES ------------------------------


# From List
data_list = [100, 102, 104, 200, 202]
series_list = pd.Series(data_list, index=['a', 'b', 'c', 'd', 'e'])

series_list.loc['c'] = 200                  
print(series_list)
print(series_list.iloc[0])                  
print(series_list[series_list >= 200])      

# From Dictionary
calories = {'day 1': 1750, 'day 2': 2100, 'day 3': 1700}
series_dict = pd.Series(calories)

series_dict.loc["day 3"] += 500             
print(series_dict)
print(series_dict.loc['day 1'])             
print(series_dict[series_dict >= 2000])     



#------------------------ DATA FRAMES ------------------------------


data_dict = {
    'name': ['spongebob', 'patrick', 'squidward'],
    'age': [30, 35, 50]
}
df = pd.DataFrame(data_dict, index=['employee 1', 'employee 2', 'employee 3'])

# New column
df['job'] = ['cook', 'N/A', 'cashier']

# New row
new_row = pd.DataFrame([{'name': 'sandy', 'age': 28, 'job': 'engineer'}], index=['employee 4'])
df = pd.concat([df, new_row])

print(df)
print(df.loc['employee 1'])                 
print(df.iloc[0])                           



#------------------------ IMPORT FILES ------------------------------



df_pokemon = pd.read_csv('datapd.csv', index_col='Name')
print(df_pokemon.to_string())

# Selection by Column (Note: 'Name' is now the index, not a column)
print(df_pokemon['Height'].to_string())
print(df_pokemon[['Height', 'Weight']].to_string())

# Selection by Rows
print(df_pokemon.loc['Moltres'])
print(df_pokemon.loc['Moltres', ['Height', 'Weight']])
print(df_pokemon.loc['Blastoise':'Moltres', ['Height', 'Weight']])
print(df_pokemon.iloc[0:12:2, 0:3])         

# Exercise
pokemon = input('Enter a name: ')
try:
    print(df_pokemon.loc[pokemon])
except KeyError:
    print(f'{pokemon} is not in the list')



#------------------------ FILTERING ------------------------------



df_filter = pd.read_csv('datapd.csv')

tall_pokemon = df_filter[df_filter['Height'] >= 2]
heavy_pokemon = df_filter[df_filter['Weight'] > 100]
legendary_pokemon = df_filter[df_filter['Legendary'] == 1]

# Logical OR (|)
water_pokemon = df_filter[(df_filter['Type1'] == 'Water') | (df_filter['Type2'] == 'Water')]

# Logical AND (&)
fire_flying_pokemon = df_filter[(df_filter['Type1'] == 'Fire') & (df_filter['Type2'] == 'Flying')]

print(fire_flying_pokemon)



#------------------------ AGGREGATION ------------------------------



df_agg = pd.read_csv("datapd.csv")

# Whole Data Frame
print(df_agg.mean(numeric_only=True))
print(df_agg.sum(numeric_only=True))
print(df_agg.min(numeric_only=True))
print(df_agg.max(numeric_only=True))
print(df_agg.count())

# Single Column
print(df_agg["Height"].mean())
print(df_agg["Height"].sum())
print(df_agg["Height"].min())
print(df_agg["Height"].max())
print(df_agg["Height"].count())

# Group By
group = df_agg.groupby("Type1")
print(group['Height'].mean())
print(group['Height'].sum())
print(group['Height'].min())
print(group['Height'].max())
print(group['Height'].count())



#---------------------------- DATA CLEANING ---------------------------------



df_clean = pd.read_csv("datapd.csv")

# 1. Drop irrelevant columns
df_clean = df_clean.drop(columns=['Legendary', 'No'], errors='ignore')

# 2. Handle missing data
df_clean = df_clean.dropna(subset=['Type2'])
df_clean = df_clean.fillna({'Type2': "none"})

# 3. Fix inconsistent values
df_clean['Type1'] = df_clean['Type1'].replace({'Grass': "GRASS", 'Fire': 'FIRE'})

# 4. Standardize text
df_clean['Name'] = df_clean['Name'].str.lower()

# 5. Fix data types
df_clean['Legendary'] = df_clean['Legendary'].astype(bool)

# 6. Removing duplicates
df_clean = df_clean.drop_duplicates()

print(df_clean.to_string())
