def f(n: int, fl: bool = True):
    if n > 21:
        return 0
    if n == 21 and fl:
        return 1
    
    if n == 26:
        fl = False
        
    return f(n + 1, fl) + f(2 * n + 1, fl)

print(f(1))

# 37
