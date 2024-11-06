def f(n: int) -> int:
    n_str = str(n)
    a = int(n_str[0])
    b = int(n_str[1])
    c = int(n_str[2])
    
    ab = a + b
    bc = b + c
    
    return int(str(min(ab, bc)) + str(max(ab, bc)))


for n in range(100, 1000):
    g = f(n)
    if g == 812:
        print(n)
        exit(0)
    
    