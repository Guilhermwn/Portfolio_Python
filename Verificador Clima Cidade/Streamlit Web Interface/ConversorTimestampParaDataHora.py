import datetime

# Valores fornecidos
sunrise_timestamp = 1697661767
sunset_timestamp = 1697574246

# Converter em data e hora
sunrise = datetime.datetime.fromtimestamp(sunrise_timestamp)
sunset = datetime.datetime.fromtimestamp(sunset_timestamp)

print("Nascer do sol:", sunrise)
print("Pôr do sol:", sunset)
