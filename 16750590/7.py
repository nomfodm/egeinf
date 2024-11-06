def f(n: int):
    n2 = bin(n)[2:]
    
    sum_ = sum([int(i) for i in n2])
    n2 = n2 + str(sum_ % 2)
    
    sum_ = sum([int(i) for i in n2])
    n2 = n2 + str(sum_ % 2)
    
    r = int(n2, 2)
    if r > 83:
        print(r)
        exit(0)
        
for n in range(1, 500):
    f(n)
    
# 86
    