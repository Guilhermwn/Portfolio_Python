# LINK: https://www.thehuxley.com/problem/1053

# Faça um programa que calcule a área da superfície e o volume de um cilindro. Use pi = 3.14.
# O valor de saída deve ser arredondado usando 2 casas decimais.

h = float(input())
r = float(input())
pi = 3.14

# Um cilindro é formado por um retângulo e dois círculos. Para calcular a área da superfície do cilindro é necessário conhecer a área de cada uma das partes que o constituem. Quanto ao cálculo da área dos círculos, o processo é relativamente simples, pois basta conhecer o raio e a fórmula matemática que nos dá essa área. Em relação ao retângulo temos que conhecer o comprimento e a largura, pois o seu produto dá-nos a área. A largura será a altura do cilindro, mas aquilo que não é evidente para muitos alunos é que o comprimento do retângulo é obtido a partir do cálculo do perímetro do círculo que é usado na base, conforme pode ser constatado na seguinte animação. Em alternativa podem sempre utilizar esta fórmula, que torna o processo de cálculo mais rápido: 
A = h*(2*pi*r) + 2*pi*(r**2)

# Para saber o volume de um cilindro, precisamos calcular o produto entre a área da base Ab e a altura h dele, porém, ao analisarmos a figura, sabemos que sua base é um círculo. A área de um círculo de raio r é calculada pela fórmula Acírculo = π r², o que justifica a fórmula para calcular-se o volume do cilindro:
V = pi*(r**2)*h

print("%.2f" % V)
print("%.2f" % A)