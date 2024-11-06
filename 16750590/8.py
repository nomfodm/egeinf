def f(n: int):
    n_str = str(n)
    
    a = int(n_str[0])
    b = int(n_str[1])
    c = int(n_str[2])
    d = int(n_str[3])
    
    ab = a + b
    bc = b + c
    cd = c + d
    
    r = int(str(min(ab, bc, cd)) + str(max(ab, bc, cd)))
    if r == 1418:
        print(n)
        exit(0)

for n in range(1000, 10000):
    f(n)
    
# 5995
    