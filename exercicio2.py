import pandas as pd
import numpy as np

''' Se uma pessoa escolhida aleatoriamente for de Alagoas ou do Pará, qual
é a probabilidade de ela ter uma renda superior a 5 mil reais?'''

df = pd.read_csv("populacao_brasileira.csv.csv")
df_alagoas_para = df[df["estado"].isin(["AL", "PA"])]
probabilidade_renda_superior =len(df_alagoas_para[df_alagoas_para["renda"]>5000])/len(df_alagoas_para)
probabilidade_complementar_renda = 1 - probabilidade_renda_superior
print (f"A probabilidade de escolher uma pessoa com renda acima de R$ 5.000 é de: {probabilidade_complementar_renda}")



