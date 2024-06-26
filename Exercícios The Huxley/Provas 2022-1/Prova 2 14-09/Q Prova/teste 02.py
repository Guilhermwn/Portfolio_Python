x = input().replace(","," ").upper().replace("A", "4").replace("O", "0").replace("E", "3").replace("I", "1").replace("S", "5").split()
c = 0
z = len(x)
d = len(x)
while 7<=z:
 for i in range(z,z-7,-1):
   c += int(x[d-i])
 print('%.2f'%(c/7))
 c = 0
 z -= 1