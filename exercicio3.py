import pandas as pd
import numpy as np
'''3. Descubra a probabilidade de uma pessoa, residente no estado do
Amazonas, ter ensino superior completo (considerando apenas a
escolaridade classificada como 'Superior'). Qual a probabilidade da quinta
pessoa amazonense que você conversar ter ensino superior completo?'''

df = pd.read_csv("populacao_brasileira.csv.csv")
df_amazonas = df[df["estado"]=="AM"]
probabilidade_ensino_superior= len(df_amazonas[df_amazonas["escolaridade"]=="Superior"])/len(df_amazonas)
probabilidade_escolaridade = 1- probabilidade_ensino_superior
print (f"A probabilidae de escolher uma pessoa amazonense com ensino superior é de: {probabilidade_escolaridade}")
print ("A probabilidade da quinta pessoa amazonense ter ensino superior completo é a mesma da primeira, segunda, terceira e quarta, pois os eventos são independentes.")



