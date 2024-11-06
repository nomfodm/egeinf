def f(n: str) -> str:
    while "111" in n or "222" in n:
        n = n.replace("111", "2", 1)\
            .replace("222", "1", 1)
            
    return n

s = "1" * 8 + "2" * 8
print(f(s))
    
    