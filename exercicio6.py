import pandas as pd
import numpy as np

'''6. Primeiro considere a probabilidade encontrada no nosso conjunto de
pessoas com escolaridade de pós-graduação. Considerando a amostra de
população brasileira com 1 milhão de habitantes, qual a probabilidade de
encontrarmos 243 mil pessoas com pós-graduação?'''

df = pd.read_csv ("populacao_brasileira.csv.csv")
df_escolaridade = df[df["escolaridade"]=="Pós-graduação"]
probabilidade_pos = len(df_escolaridade[df_escolaridade["escolaridade"] == "Pós-graduação"])/len(df_escolaridade)
probabilidade_pos = len(df_escolaridade) / len(df)
print (f"As chances de encontrar alguém com pós-graduação é de: {probabilidade_pos}")

def calcular_probabilidade_pos_graduacao(populacao_amostra, pessoas_pos_graduacao):

  return pessoas_pos_graduacao / populacao_amostra

# Dados da amostra
populacao_amostra = 1000000
pessoas_pos_graduacao = 243000

# Calcula a probabilidade
probabilidade = calcular_probabilidade_pos_graduacao(populacao_amostra, pessoas_pos_graduacao)

# Imprime o resultado
print(f"A probabilidade de encontrar 243 mil pessoas com pós-graduação em 1 milhão é: {probabilidade:.3f}")