from functools import lru_cache


@lru_cache(None)
def f(n: int) -> int:
    if n == 0:
        return 1
    
    if n % 2 != 0:
        return (n % 10) * f(n // 100)
    
    if n > 0 and n % 2 == 0:
        return f(n // 100)
    
    
answer = 0
for i in range(10_000_000, 8 * 10_000_000 + 1):
    if f(i) == 35:
        answer += 1
        
print(answer)
    
    