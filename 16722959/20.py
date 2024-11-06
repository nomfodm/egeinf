from functools import lru_cache


@lru_cache
def f(n: int) -> int:
    if n < 3:
        return 1
    
    if n > 2 and n % 2 != 0:
        return f(n - 1) + 3 * f(n - 2)
    
    if n > 2 and n % 2 == 0:
        return sum([f(i) for i in range(1, n)])
    
for i in range(30):
    f(i)
    
print(f(28))
    
    
    