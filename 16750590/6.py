def f(n: int):
    n2 = bin(n)[2:]
    if n2.count("0") >= n2.count("1"):
        n2 = n2 + "0"
    else:
        n2 = n2 + "1"
        
    r = int(n2, 2)
    if r > 100:
        print(r)
        exit(0)

for n in range(1, 500):
    f(n)
    
# 103
        