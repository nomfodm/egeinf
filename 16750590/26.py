def f(n: int):
    if n == 0:
        return 0
    if n % 2 == 0:
        return f(n // 2)
    return 1 + f(n - 1)
    
for n in range(0, 10000):
    if f(n) == 11:
        print(n)
        break
    
# 2047
    