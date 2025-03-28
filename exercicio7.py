import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ("populacao_brasileira.csv.csv")

'''Somando as densidades nós temos a função de densida de acumulada.
Considerando a coluna ‘Escolaridade’ faça a função de densidade
acumulada discreta para cada nível de escolaridade.'''

frequencia_escolaridade = df["escolaridade"].value_counts().sort_index()
cdf_escolaridade = frequencia_escolaridade.cumsum() / len(df)
plt.figure(figsize=(10, 6))
plt.plot(cdf_escolaridade.index, cdf_escolaridade.values, marker='o')
plt.title("Função de Densidade Acumulada da Escolaridade")
plt.xlabel("Nível de Escolaridade")
plt.ylabel("Probabilidade Acumulada")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

print("Função de Densidade Acumulada da Escolaridade:")
print(cdf_escolaridade)