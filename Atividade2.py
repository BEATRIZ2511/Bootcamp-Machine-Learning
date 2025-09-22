Atividade 2 - 

1- Escreva uma função que receba uma lista de números e retorne outra lista 
com os números ímpares.
R=
def filtrar_impares(lista):
   impares = []
    for numero in lista:
        if numero % 2 != 0:  # verifica se o número é ímpar
            impares.append(numero)
    return impares

numeros = [1, 2, 3, 4, 5, 6, 7]
print(filtrar_impares(numeros))  # Saída: [1, 3, 5, 7]

  2 -  Escreva uma função que receba uma lista de números e retorne outra lista 
com os números primos presentes.
R= 
def eh_primo(n):
    if n < 2:  
        return False  
    
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
def filtrar_primos(lista):
    primos = []
    for numero in lista:
        if eh_primo(numero):
            primos.append(numero)
    return primos
numeros = [1, 2, 3, 4, 5, 6, 7, 15, 19, 20]
print(filtrar_primos(numeros))

3. Escreva uma função que receba duas listas e retorne outra lista com os 
elementos que estão presentes em apenas uma das listas.
R=
def apenas_uma_lista(lista1, lista2):
    resultado = []

    for x in lista1:
        if x not in lista2:
            resultado.append(x)
    
    for x in lista2:
        if x not in lista1:
            resultado.append(x)
    
    return resultado
def apenas_uma_lista(lista1, lista2):
    return list(set(lista1) ^ set(lista2))  # ^ é diferença simétrica
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

print(apenas_uma_lista(a, b))

4. Dada uma lista de números inteiros, escreva uma função para encontrar o 
segundo maior valor na lista.
R=
def segundo_maior(lista):
    lista_unica = list(set(lista))
    lista_unica.sort(reverse=True)
    
    return lista_unica[1]
numeros = [10, 20, 4, 5, 20, 3, 5]
print(segundo_maior(numeros))

5. Crie uma função que receba uma lista de tuplas, cada uma contendo o 
nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das 
pessoas em ordem alfabética.
  R=
def ordenar_por_nome(lista):
    lista.sort(key=lambda x: x[0])
    return lista
pessoas = [("Ana", 25), ("Carlos", 30), ("Beatriz", 22), ("David", 28)]
print(ordenar_por_nome(pessoas))

6. Como identificar e tratar outliers em uma coluna numérica usando desvio 
padrão ou quartis? 
R=
import numpy as np

dados = [10, 12, 13, 15, 20, 22, 25, 100, 30, 35, 40]

media = np.mean(dados)
desvio_padrao = np.std(dados)

limite_superior = media + 3 * desvio_padrao
limite_inferior = media - 3 * desvio_padrao

outliers = [x for x in dados if x < limite_inferior or x > limite_superior]

print(f"Outliers identificados: {outliers}")

dados_tratados = [min(max(x, limite_inferior), limite_superior) for x in dados]
print(f"Dados tratados: {dados_tratados}")

7. Como concatenar vários DataFrames (empilhando linhas ou colunas), 
mesmo que tenham colunas diferentes? 
Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 
(colunas). Quando há colunas diferentes, os valores ausentes são 
preenchidos com NaN.
  R=
import pandas as pd

# Concatenar por linhas (axis=0)
df1 = pd.DataFrame({"id": [1, 2], "nome": ["Ana", "Bia"]})
df2 = pd.DataFrame({"id": [3, 4], "nome": ["Carlos", "Daniel"]})
resultado1 = pd.concat([df1, df2], axis=0)
print(resultado1)

# Concatenar por colunas (axis=1)
df3 = pd.DataFrame({"idade": [23, 25, 30]})
df4 = pd.DataFrame({"cidade": ["SP", "RJ", "BH"]})
resultado2 = pd.concat([df3, df4], axis=1)
print(resultado2)

# Concatenar DataFrames com colunas diferentes
df5 = pd.DataFrame({"id": [1, 2], "nome": ["Ana", "Bia"]})
df6 = pd.DataFrame({"id": [3, 4], "idade": [20, 22]})
resultado3 = pd.concat([df5, df6], axis=0)
print(resultado3)

8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um 
DataFrame e exibir as primeiras linhas?  
R=
import pandas as pd

df = pd.read_csv("dados.csv")

print(df.head())

9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas 
em um “DataFrame” com base em uma condição? 
R=
Podemos selecionar uma coluna específica de um DataFrame usando a notação de colchetes df["coluna"].
Para filtrar linhas com base em uma condição, usamos uma expressão lógica dentro dos colchetes.

import pandas as pd

df = pd.DataFrame({
    "nome": ["Ana", "Bia", "Carlos", "Daniel"],
    "idade": [23, 25, 17, 30]
})

coluna_idade = df["idade"]
print("Coluna idade:")
print(coluna_idade)

# Filtrar linhas onde a idade seja maior ou igual a 18
filtro = df[df["idade"] >= 18]
print("\nPessoas com 18 anos ou mais:")
print(filtro)

10. Utilizando pandas, como lidar com valores ausentes (NaN) em um 
DataFrame?
R=
import pandas as pd

# Criando um DataFrame com valores ausentes
df = pd.DataFrame({
    "nome": ["Ana", "Bia", "Carlos", None],
    "idade": [23, None, 30, 25]
})

# Remover linhas com qualquer NaN
df_sem_nan = df.dropna()
print("Sem NaN (linhas removidas):")
print(df_sem_nan)

# Remover colunas com qualquer NaN
df_sem_colunas = df.dropna(axis=1)
print("\nSem NaN (colunas removidas):")
print(df_sem_colunas)

# Preencher NaN com um valor fixo
df_preenchido = df.fillna("Desconhecido")
print("\nValores preenchidos:")
print(df_preenchido)

# Preencher NaN na coluna "idade" com a média
df["idade"] = df["idade"].fillna(df["idade"].mean())
print("\nIdades preenchidas com a média:")
print(df)


