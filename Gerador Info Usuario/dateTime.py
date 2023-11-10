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

# Supondo que date_time contenha a data e hora no formato dado
date_time_str = "2023-10-15T12:11:35.293126-03:00"

# Converter a string em um objeto datetime
date_time_obj = datetime.fromisoformat(date_time_str)

# Formatar a data e hora para exibição
formatted_date_time = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")

# Obter o número do mês a partir do objeto datetime
month_number = date_time_obj.month
day_number = date_time_obj.day
year_number = date_time_obj.year

hours = date_time_obj.hour
minutes = date_time_obj.minute
seconds = date_time_obj.second

# Obter o nome do mês a partir do dicionário
month_name = month_names[month_number]

# Mostra a data
print(f"Data: {day_number} de {month_name} de {year_number}")
print(f"Hora Atual: {hours} horas {minutes} minutos e {seconds} segundos")


