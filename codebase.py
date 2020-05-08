import pandas as pd

'''Loading the data from CSV,EXCEL and TXT'''
pokemon_df = pd.read_csv("pokemon_data.csv")
pokemon_df_excel = pd.read_excel("pokemon_data.xlsx")
pokemon_df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")
print(pokemon_df_txt.head(3))
