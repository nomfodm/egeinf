def f(n: int) -> int:
    n2 = bin(n)[2:]
    n2 = n2 + n2[-2]
    n2 = n2 + n2[1]
    
    r = int(n2, 2)
    return r

for n in range(2, 500):
    g = f(n)
    if g > 180:
        print(n)
        break
    
    
    