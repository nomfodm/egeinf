def f(n: str) -> str:
    while "111" in n:
        n = n.replace("111", "2", 1)\
            .replace("222", "11", 1)
            
    return n

print(f("1" * 78))

# 2211
