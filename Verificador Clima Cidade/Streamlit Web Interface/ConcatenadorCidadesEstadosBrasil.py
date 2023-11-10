import pandas as pd

# Lê o arquivo CSV com ponto e vírgula como separador
df = pd.read_csv('cidadesBrasil.csv', sep=';')

# Obtém as séries de nome da cidade e sigla do estado
cidade_series = df['Municipio']
estado_series = df['UF']

cidade_UF_serie = cidade_series.str.cat(estado_series, sep=' - ')

print(cidade_UF_serie.head())

valor1 = df.at[2, 'Municipio']  # Lembre-se de que o índice começa em 0, então a terceira linha é o índice 2

# Acessar o valor na linha 7, coluna 'Municipio'
valor2 = df.at[6, 'Municipio']

print("Valor na linha 3, coluna 'Municipio':", valor1)
print("Valor na linha 7, coluna 'Municipio':", valor2)