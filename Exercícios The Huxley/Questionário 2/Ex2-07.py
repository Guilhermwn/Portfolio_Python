# LINK: https://www.thehuxley.com/problem/305


# == EXPLICAÇÃO DO CÓDIGO ==
# Este código calcula e exibe o tempo em horas, minutos e segundos 
# com base em um valor inteiro de tempo em segundos fornecido pelo usuário.


tempo = int(input())

horas = int(tempo/3600)
tempo = tempo % 3600

minutos = int(tempo/60)
tempo = tempo % 60

segundos = tempo

print(f"{horas}:{minutos}:{segundos}")