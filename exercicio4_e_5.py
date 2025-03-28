import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

df = pd.read_csv("populacao_brasileira.csv.csv")

'''4. Considerando a renda das pessoas do nosso conjunto, podemos dizer
que a renda de uma pessoa brasileira está na sua maioria em que faixa
(faça faixa de 1.500 reais)? Qual é a sua função densidade de probabilidade?'''

faixas_de_renda = list(range(0, int(df["renda"].max())+1500,1500))
labels_faixas = [f"{i}-{i+1500}" for i in faixas_de_renda[:-1]]
df["faixa_renda"] = pd.cut(df["renda"], bins=faixas_de_renda, labels=labels_faixas, right=False)

#calculando a frequência de cada faixa de renda.
frequencia_faixas = df["faixa_renda"].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="faixa_renda", order=labels_faixas)
plt.title("Distribuição de Renda no Brasil")
plt.xlabel("Faixa de Renda (R$)")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.figure(figsize=(12, 6))
sns.histplot(data=df, x="renda", bins=faixas_de_renda, stat="density")
plt.title("Função Densidade de Probabilidade da Renda no Brasil")
plt.xlabel("Renda (R$)")
plt.ylabel("Densidade de Probabilidade")
plt.tight_layout()
plt.show()

'''5. Calcule a média e a variância da renda da amostra. Depois faça a
distribuição normal, inclua o gráfico'''

media_renda = df["renda"].mean()
variancia_renda = df["renda"].var()

print(f"Média da renda: {media_renda:.2f}")
print(f"Variância da renda: {variancia_renda:.2f}")
desvio_padrao_renda = np.sqrt(variancia_renda)
distribuicao_normal = norm(media_renda, desvio_padrao_renda)
valores_x = np.linspace(df["renda"].min(), df["renda"].max(), 100)
pdf_normal = distribuicao_normal.pdf(valores_x)
plt.figure(figsize=(12, 6))
sns.histplot(df["renda"], bins=30, kde=False, stat="density", color="skyblue", label="Histograma da Renda")
plt.plot(valores_x, pdf_normal, color="red", label="Distribuição Normal")
plt.title("Distribuição Normal da Renda")
plt.xlabel("Renda")
plt.ylabel("Densidade de Probabilidade")
plt.legend()
plt.tight_layout()
plt.show()
