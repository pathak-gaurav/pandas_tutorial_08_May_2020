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

print(pokemon_df.loc[pokemon_df['Type 1'] == 'Grass'])
