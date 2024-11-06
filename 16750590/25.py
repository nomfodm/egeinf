def f(n: int):
    if n == 1:
        return 1
    return f(n - 1) + 2 ** (n - 1)
    
print(f(10))

# 1023
