def f(n: str) -> str:
    while "722" in n or "557" in n:
        n = n.replace("722", "57", 1)\
            .replace("557", "72", 1)
            
    return n

print(f("5" * 54 + "7"))

# 572
    