# link: https://www.thehuxley.com/problem/3672
nInscritos = int(input())

#coleta CPF
cpf = ''
cpfLista = list()
for i in range(nInscritos):
    cpf = int(input())
    cpfLista.append(cpf)

#coleta a nota 
nota = ''
notaLista = list()
for i in range(nInscritos):
    nota = int(input())
    notaLista.append(nota)


mVezes = int(input())
mTestes =''
mLista = list()
for i in range(mVezes):
    mTestes = int(input())
    mLista.append(mTestes)



candidatos = list(zip(cpfLista, notaLista))

for i in cpfLista:
