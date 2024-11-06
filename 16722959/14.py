from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n == 1:
        return 2
    
    if n >= 2:
        return f(n - 1) * n

    
for i in range(1, 10):
    f(i)
    
print(f(5))   
