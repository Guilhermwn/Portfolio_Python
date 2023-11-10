import random

cores = ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul", "Rosa", "Marrom", "Ciano", "Branco", "Preto", "Cinza"]
dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
cores_dias = []

random.shuffle(cores)

for i in range(len(dias_da_semana)):
    cores_dias.append(cores[i])
    print(f"{dias_da_semana[i]} usarei camisa da cor {cores_dias[i]}")
