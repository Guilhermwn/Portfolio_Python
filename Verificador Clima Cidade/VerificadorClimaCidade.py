import requests
import time
import os

# PERGUNTA SE DESEJA UM TUTORIAL
print('Deseja um tutorial de como proceder?')
time.sleep(2)
tutorial = input('Sim(y) ou Não(n)\n')
time.sleep(1)
os.system('cls')

# IF PARA ESCOLHER SE VAI APARECER UM TUTORIAL OU NÃO
if tutorial == 'y':
    print(""" 
  ---------------------
  |   SIGA O MODELO   |
  ---------------------
  """)
    time.sleep(2)
    print("SISTEMA -> Digite o nome da cidade a verificar o clima: ")
    time.sleep(2)
    print('VOCÊ -> manaus')
    time.sleep(2)
    print('\n-- APARECERÁ OS DADOS DO CLIMA DA CIDADE SELECIONADA --')
    time.sleep(5)
    os.system('cls')
    print('Bem vindo ao Verificador de Clima')
else:
    os.system('cls')
    print('Bem vindo ao Verificador de Clima')

# CÓDIGO PRINCIPAL DO BetaWeather
# NOME DA CIDADE A VERIFICAR O CLIMA
while 1 != 2:
    cidade_clima = str(input("Digite o nome da cidade a verificar o clima: "))

    # CRIAÇÃO DO LINK DE VERIFICAÇÃO DA API OPENWEATHERMAP.ORG
    api_link = "http://api.openweathermap.org/data/2.5/weather?appid=9ed06dc6e0e2d16f22f237aba9d94702&lang=pt_br&units=metric&q="
    url = api_link + cidade_clima

    # REQUEST DO ARQUIVO JSON GERADO PELA API
    json_daApi = requests.get(url).json()

    # DADOS RETIRADOS DO ARQUIVO JSON
    clyma = json_daApi['weather'][0]['description']
    temp_atual = json_daApi['main']['temp']
    termica_feels = json_daApi['main']['feels_like']
    humidadi = json_daApi['main']['humidity']
    ventu = json_daApi['wind']['speed']
    cidade = json_daApi['name']
    pais = json_daApi['sys']['country']

    # HORARIO DO DIA(se está de dia ou de noite)
    hora = json_daApi['dt']
    por_sol = json_daApi['sys']['sunset']

    # ---------------------------------------#
    # INÍCIO DA RESPOSTA
    # MOSTRA VALORES RELACIONADAS A LOCALIZAÇÃO DA CIDADE VERIFICADA
    print('\n☁️ LOCALIZAÇÃO☁️')
    print('Cidade: {}'.format(cidade))
    print('País: {}'.format(pais))
    print('')

    # MOSTRA VALORES RELACIONADOS AO CLIMA DA CIDADE VERIFICADA
    time.sleep(1)
    print('☁️️️️ ️️️️️CLIMA☁️')
    print('Clima: {}'.format(clyma))
    print('')

    # MOSTRA VALORES RELACIONADOS AO CLIMA DA CIDADE VERIFICADA
    time.sleep(1)
    print('☁️️️️ ️️️️️TEMPERATURA☁️')
    print('Temperatura atual: {}ºC'.format(temp_atual))
    print('Sensação térmica: {}ºC'.format(termica_feels))
    print('')

    # MOSTRA VALORES EXTRA RELACIONADAS
    time.sleep(1)
    print('☁️️️️ ️️️️️EXTRAS☁️')
    print('Humidade: {}%'.format(humidadi))
    print('Vento: {} Km/h'.format(ventu))

    # COMPARA OS DADOS DE TIMEZONE DA HORA ATUAL COM OS DADOS DE TIMEZONE DO PÔR DO SOL E VERIFICA SE ESTÁ DE NOITE OU DE DIA
    if hora < por_sol:
        print('Em {} está de dia agora'.format(cidade_clima))
    else:
        print('Em {} está de noite agora'.format(cidade_clima))

    # CONDIÇÃO QUE PERGUNTA AO USER SE DESEJA VERIFICAR O CLIMA DE OUTRA CIDADE
    time.sleep(3)
    print('--------------------------------------------')
    print('\nDeseja verificar o clima de outra cidade?')
    denovo = input('sim(y) ou Não(n)\n')
    if denovo == 'y':
        time.sleep(1)
        print('OK')
        time.sleep(3)
        os.system('cls')
    else:
        time.sleep(1)
        print('OK')
        time.sleep(2)
        print('Obrigado por usar o programa Verificador de Clima!!')
        break
