from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n < 11:
        return 10
    
    return n + f(n - 1)

for i in range(2100):
    f(i)


print(f(2021) - f(2019))    

    