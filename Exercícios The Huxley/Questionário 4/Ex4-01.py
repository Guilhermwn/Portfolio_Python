energia = float(input())

nn = energia * 1.35
dnn = energia * 1.55

qsq = energia * 1.75 
qsqa = qsq + (qsq * (10/100))

qsc = energia * 2.15
qsca = qsc + (qsc * (10/100))

if energia < 25.94:
    print(35)
    print(1.35)
elif energia < 100:
    print("%.2f" % nn)
    print(1.35)
elif energia >= 100 and energia < 300:
    print("%.2f" % dnn)
    print(1.55)
elif energia == 300:
    print("%.2f" % qsq)
    print(1.75)
elif energia > 300 and energia < 575:
    print("%.2f" % qsqa)
    print(1.75)
elif energia >= 575:
    print("%.2f" % qsca)
    print(1.75)

# 0 = 35; 1.35 +
# 50 = 67.50; 1.35 +
# 99 = 133.65; 1.35 +
# 100 = 155; 1.55 +
# 200 = 310; 1.55 +
# 299 = 463.45; 1.55 +
# 300 = 525; 1.75 +
# 570 = 1097.25; 1.75
# 574 = 1104.95; 1.75
# 575 = 1359.88; 2.15