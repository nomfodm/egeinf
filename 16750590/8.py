def f(n: int):
    n_str = str(n)
    
    a = int(n_str[0])
    b = int(n_str[1])
    c = int(n_str[2])
    d = int(n_str[3])
    
    ab = a + b
    bc = b + c
    cd = c + d
    
    g = [ab, bc, cd]
    
    h = str(max(g))
    g.remove(max(g))
    j = str(max(g))
    
    if int(j + h) == 1418:
        print(n)
        exit(0)

for n in range(1000, 10000):
    f(n)

# 5995
    