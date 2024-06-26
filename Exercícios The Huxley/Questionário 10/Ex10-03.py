def vantagem(candidato, concorrente, n):
    vantagem = candidato[0]-concorrente[0]
    
    for i in range(n):
        if candidato[i]-concorrente[i]>vantagem:
            vantagem = candidato[i]-concorrente[i]
    
    if vantagem < 0:
        return 0
    else:
        return vantagem


n = int(input())
candidato_str, concorrente_str = input().split(), input().split()

candidato = [float(n) for n in candidato_str]
concorrente = [float(n) for n in concorrente_str]

print ("%.2f" % vantagem(candidato, concorrente, n))