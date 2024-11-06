def f(n: int, f1: bool = False, f2: bool = True):
    if n > 21:
        return 0
    if n == 21 and f1 and f2:
        return 1
    
    if n == 10:
        f1 = True
        
    if n == 16:
        f2 = False
        
    return f(n + 1, f1, f2) + f(n * 2, f1, f2)

print(f(1))

# 14
