ano = int(input())
bissexto = ano % 4

exc1 = ano % 100 
exc2 = ano % 400

if (bissexto == 0 and exc1 != 0) or (exc2 == 0):
    print("BISSEXTO")
else:
    print("NAOBISSEXTO")