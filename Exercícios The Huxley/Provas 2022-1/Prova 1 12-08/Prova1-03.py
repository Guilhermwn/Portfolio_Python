def velocidadeinicial(S, Si, a, t):
    vel = ((S-Si) / t) - ((a * (t**2) / 2) / t)
    return vel

S = float(input())
Si = float(input())
a = float(input())
t = float(input())

vel = velocidadeinicial(S, Si, a, t)
print("Velocidade inicial: %.2fm/s" % vel)