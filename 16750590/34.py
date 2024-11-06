def f(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 1
    
    return f(n - 2) + f(n - 5)

print(f(23))

# 29
