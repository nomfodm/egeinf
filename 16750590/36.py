def f(n: int, fl: bool = False):
    if n < 5:
        return 0
    if n == 5 and fl:
        return 1
    
    if n == 33:
        fl = True
        
    return f(n - 1, fl) + f(n // 3, fl)

print(f(67))

# 20
