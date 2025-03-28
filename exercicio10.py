import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



'''10. Qual é a probabilidade de escolhermos uma pessoa residente na região
Sudeste que seja homem, tenha apenas ensino fundamental completo e
possua renda mensal superior a 2 mil reais?'''

df =pd.read_csv("populacao_brasileira.csv.csv")

df_sudeste =["ES", "SP","MG", "RJ"]
df_região = df[df["estado"].isin(df_sudeste)]

df_perfil = df_região[
    (df_região["sexo"] == "M") &
    (df_região["escolaridade"] == "Fundamental") &
    (df_região["renda"] > 2000)
]

probabilidade_perfil = len(df_perfil) / len(df_sudeste)

print(f"A probabilidade do perfil mencionado na questão é de: {probabilidade_perfil:.4f}")
print(f"A probabilidade do perfil mencionado na questão é de: {probabilidade_perfil}")