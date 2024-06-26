def inverter(xs):
    inverterDeAte(0, len(xs)-1, xs)

def inverterDeAte(i, j, xs):
 if i < j:
    xs[i], xs[j] = xs[j], xs[i]
    inverterDeAte(i+1, j-1, xs)

xs = [1,2,3]
inverter(xs)