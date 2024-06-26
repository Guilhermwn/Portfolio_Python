contador = 0
conta = 0
final = 5
#variáveis adicionadas, porque estava dando como não declaradas, dentro do while
while True:
    call = input()
    check = call.isnumeric() #função .isnumeric() usada para checar se a entrada era um número ou o '*'

    if check == True:
        if contador >= 5:
            conta = (int(call) * 0.5 )
        final = final + conta #variável 'final' adicionada para somar o resultado da conta

    elif check == False:
        if call == "*":
            break   

    contador += 1

if final > 50:
    final = final - (final * 0.2)

elif final == 0:
    final = 5

print("%.2f" % final)