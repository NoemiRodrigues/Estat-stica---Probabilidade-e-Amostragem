import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("populacao_brasileira.csv.csv")

'''Qual a margem de erro amostral da proporção populacional
considerando a proporção de pessoas com nível de inglês intermediário?'''

df_ingles = df[df["nível de proficiência em inglês"].isin(["Intermediário"])]
proporcao_ingles_intermediario = len(df_ingles) / len(df)

def calcular_margem_erro(proporcao, tamanho_amostra, nivel_confianca):
    if nivel_confianca == 95:
        z = 1.96
    elif  nivel_confianca == 99:
        z = 2.58
  

    margem_erro = z * np.sqrt((proporcao * (1 - proporcao)) / tamanho_amostra)
    return margem_erro

# Dados
tamanho_amostra = len(df)  # Usando o tamanho total do DataFrame como tamanho da amostra
nivel_confianca = 95

# Calcula a margem de erro
margem_erro = calcular_margem_erro(proporcao_ingles_intermediario, tamanho_amostra, nivel_confianca)

# Imprime o resultado
print(f"A proporção de pessoas com inglês intermediário é: {proporcao_ingles_intermediario:.4f}")
print(f"A margem de erro para um nível de confiança de {nivel_confianca}% é: {margem_erro:.4f}")