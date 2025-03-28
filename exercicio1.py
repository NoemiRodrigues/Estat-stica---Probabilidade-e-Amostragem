import pandas as pd
import numpy as np

'''Considere pessoas fluentes em inglês, qual a probabilidade
complementar? Ou seja, qual a probabilidade de escolhermos uma pessoa
aleatória e ela não ser fluente em inglês. Considere fluente quem tem o
nível avançado.'''

df = pd.read_csv("populacao_brasileira.csv.csv")
fluencia_probabilidade = len(df[df["nível de proficiência em inglês"]== "Avançado"])/len(df)
probabilidade_complementar = 1 - fluencia_probabilidade

print(f"A probabilidade de escolher uma pessoa não fluente em inglês é: {probabilidade_complementar}")