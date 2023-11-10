import requests
import funictions
import random


#dados do User
Discord = input("Insira seu Nome do Discord: ")
Noame = input("Insira seu nome: ")

# criar link da api
auth = '6b55cfea-e85c-4a8f-b015-7d5f5dcdf770'  # key da api (pode mudar de acordo com o usuario)
url = 'https://api.ipfind.com/me?auth=' + auth  # URL final
response = requests.get(url).json()

# coleta as informações do JSON criado pela api
ipaddres = response["ip_address"]  # endereço ip
cidaty = response["city"]  # cidade
regioon = response["region"]  # região/estado

# api do horario e data
date_url = 'http://worldtimeapi.org/api/ip'

# dados da data e hora
date_response = requests.get(date_url).json()
date_hora = date_response["datetime"]

# nome do arquivo a ser criado
numbeer = random.randint(1, 100)  # número que aleatoriza para o nome do arquivo
FILE_NAME = str(numbeer) + " - " + Noame + ".txt"  # exato nome do file

# cria o arquivo e adiciona dados nele
funictions.Create_File(FILE_NAME, Discord, Noame)
funictions.Append_InFile(FILE_NAME, ipaddres, cidaty, regioon, date_hora)

# sinaliza que o arquivo foi gerado com sucesso
print("Arquivo gerado com sucesso!")
