def f(n: int):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    return 2 * f(n - 2)

print(f(26))

# 4122
