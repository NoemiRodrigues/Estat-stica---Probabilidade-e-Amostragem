import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv ("populacao_brasileira.csv.csv")

''' Calcula a renda da população. Qual a probabilidade de encontrar 60
pessoas com uma renda mil reais superior à média?'''

media_renda = df["renda"].mean()

# Filtra as pessoas com renda mil reais superior à média
df_renda_superior = df[df["renda"] > (media_renda + 1000)]

# Calcula a probabilidade de encontrar uma pessoa com renda mil reais superior à média
probabilidade_renda_superior = len(df_renda_superior) / len(df)

probabilidade_60_pessoas = probabilidade_renda_superior ** 60

print(f"Média da renda: R$ {media_renda:.2f}")
print(f"Probabilidade de encontrar uma pessoa com renda mil reais superior à média: {probabilidade_renda_superior:.4f}")
print(f"Probabilidade de encontrar 60 pessoas com renda mil reais superior à média: {probabilidade_60_pessoas:.4e}")


plt.figure(figsize=(10, 6))
plt.hist(df["renda"], bins=30, edgecolor="black")
plt.axvline(media_renda, color="red", linestyle="dashed", linewidth=2, label=f"Média: R$ {media_renda:.2f}")
plt.axvline(media_renda + 1000, color="green", linestyle="dashed", linewidth=2, label=f"Média + R$ 1.000")
plt.title("Distribuição da Renda")
plt.xlabel("Renda (R$)")
plt.ylabel("Frequência")
plt.legend()
plt.tight_layout()
plt.show()