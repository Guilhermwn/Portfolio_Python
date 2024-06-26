def printf(t):
    print(t, end="")
    
n = int(input())
i=1
num=0
den=0
s=0

while i<=n:
    num+=1
    den+=3
    s+=(num)/(den)
    i+=1
    
    if i<=n:
        printf("%.0d/%.0d" % (num, den))
    
    if i<=n:
        printf(" + ")
    
    else:
        print("%.0d/%.0d" % (num, den))
    
    
print("%.2f" % s)