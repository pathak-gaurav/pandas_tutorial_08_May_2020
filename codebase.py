import pandas as pd

'''Loading the data from CSV,EXCEL and TXT'''
pokemon_df = pd.read_csv("pokemon_data.csv")
# pokemon_df_excel = pd.read_excel("pokemon_data.xlsx")
# pokemon_df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")
# print(pokemon_df_txt.head(3))

''' Reading Headers '''
# print(pokemon_df.columns)

''' Reading Specific Column Values '''
# print(pokemon_df['Name'][0:10])

''' Reading Multiple Column Values '''
# print(pokemon_df[['Name','Defense']][0:10])

''' Getting specific rows '''
# print(pokemon_df.iloc[3])
# print(pokemon_df.iloc[1:4])

''' Reading a data within a specific row '''
# print(pokemon_df.iloc[2,1])

'''Iterate over DataFrame rows'''
# for index,row in pokemon_df.iterrows():
    # print(index,row['Name'])


'''Accessing Rows where type1 is fire'''
# print(pokemon_df.loc[pokemon_df['Type 1'] == "Fire"])

# print(pokemon_df.loc[pokemon_df['Type 1'] == 'Grass'])


'''Sorting & describing Data'''
# print(pokemon_df.describe())

'''Sorting by Name'''
# print(pokemon_df.sort_values('Name').head(5))
# print(pokemon_df.sort_values('Name').tail(5))

'''Sorting by Name Descending'''
# print(pokemon_df.sort_values('Name',ascending=False))

'''Sorting two fields'''
# print(pokemon_df.sort_values(['Type 1','HP'],ascending=[1,0]))


'''======================='''
'''Making Changes to Data'''
'''======================='''

# print(pokemon_df.columns)
'''Adding a Column in DF'''
pokemon_df['Total'] = pokemon_df['HP'] + pokemon_df['Attack'] + pokemon_df['Defense'] + pokemon_df['Sp. Atk'] + \
                      pokemon_df['Sp. Def'] + pokemon_df['Speed']

'''Dropping the added Column'''
# pokemon_df = pokemon_df.drop(columns=['Total'])

'''Adding Column through indexing'''
# pokemon_df['Total'] = pokemon_df.iloc[:, 4:10].sum(axis=1)
# print(pokemon_df.head(5))

'''Getting Column as List'''
col = list(pokemon_df.columns)
# # print(col)
pokemon_df = pokemon_df[col[0:4] + [col[-1]] + col[4:12]]
# print(pokemon_df.columns)

'''========================='''
'''Saving and Exporting Data'''
'''========================='''

# pokemon_df.to_csv("modified-total-column.csv")

'''Saving Excel without Index Column'''
# pokemon_df.to_excel("modified-total-column.xlsx",index=False)

'''Saving file as a txt'''
pokemon_df.to_csv('modified-total-column.txt',index=False,sep='\t')