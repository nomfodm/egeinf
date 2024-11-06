def f(n):
    if n == 0:
        return 1
    if n % 2 != 0:
        return (n % 10)*f(n // 100)
    return f(n // 100)

counter = 0   
for x in range(10 ** 7, 8 * 10 ** 7 + 1):
    if f(x) == 35:
        counter += 1
        
print(counter)

# 3024000
