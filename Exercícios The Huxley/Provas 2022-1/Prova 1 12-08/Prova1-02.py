gas = int(input())

if gas < 10:
    print(5)
elif gas >= 11 and gas <= 50:
    print(5 + (gas - 10))

elif gas >= 51 and gas <= 80:
    print(45 + ((gas - 50) * 2))

elif gas >= 81:
    print(105 + ((gas - 80) * 3))