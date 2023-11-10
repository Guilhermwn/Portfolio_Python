import requests
import new_file
import random
from datetime import datetime

# Dicionário de nomes dos meses
month_names = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

#dados do User
nome_usuario = input("Insira seu nome: ")
idade = input("Insira sua idade: ")

# ============== API DE BUSCA DE IP ==============#
# criar link da api
api_key = '6b55cfea-e85c-4a8f-b015-7d5f5dcdf770'  # key da api (pode mudar de acordo com o usuario)
api_url = 'https://api.ipfind.com/me?auth=' + api_key  # URL final
response = requests.get(api_url).json()

# coleta as informações do JSON criado pela api
ip_addres = response["ip_address"]  # endereço ip
cidade = response["city"]  # cidade
regiao = response["region"]  # região/estado
# ============== API DE BUSCA DE IP ==============#

# ============== API DE BUSCA DE TIMEZONE ==============#
# api do horario e data
date_url = 'http://worldtimeapi.org/api/ip'

# dados da data e hora
date_response = requests.get(date_url).json()
date_hora = date_response["datetime"]

# Converter a string em um objeto datetime
date_time_obj = datetime.fromisoformat(date_hora)

# Obter o ano, mês e dia a partir do objeto datetime
year_number = date_time_obj.year
month_number = date_time_obj.month
day_number = date_time_obj.day

# Obter horas, minutos e segundos a partir do objeto datetime
hours = date_time_obj.hour
minutes = date_time_obj.minute
seconds = date_time_obj.second

# Obter o nome do mês a partir do dicionário
month_name = month_names[month_number]

data = f"Data Atual: {day_number} de {month_name} de {year_number}"
horario = f"Hora Atual: {hours} horas {minutes} minutos e {seconds} segundos"
# ============== API DE BUSCA DE TIMEZONE ==============#

# ============== CRIAÇÃO DO ARQUIVO ==============#
# nome do arquivo a ser criado
random_number = random.randint(1, 100)  # número que aleatoriza para o nome do arquivo
FILE_NAME = str(random_number) + " - " + nome_usuario + ".txt"  # exato nome do file

# cria o arquivo e adiciona dados nele
new_file.Create_File(FILE_NAME, idade, nome_usuario)
new_file.Append_InFile(FILE_NAME, ip_addres, cidade, regiao, data, horario)
# ============== CRIAÇÃO DO ARQUIVO ==============#

# sinaliza que o arquivo foi gerado com sucesso
print("Arquivo gerado com sucesso!")
