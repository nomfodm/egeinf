from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n >= 2000:
        return 2000
    
    if n % 2 != 0:
        return n * f(n + 1)
    
    if n % 2 == 0:
        return n * f(n + 1) // 2


for i in range(2100, 1, -1):
    f(i)
    
print(f(1998) // f(2001))
