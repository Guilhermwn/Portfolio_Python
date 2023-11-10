# LINK: https://www.thehuxley.com/problem/32
# Converter uma temperatura dada em graus Fahrenheit para graus Celsius.


faren = float(input())
#°C = (°F − 32) ÷ 1, 8

celsius = (faren - 32) / 1.8

print("%.2f" % celsius)