def f(p: int):
    return int("AB967D8", p) + int("E435A98", p)

for p in range(15, 36):
    if f(p) % (p - 1):
        print(p)
        break

# 15
