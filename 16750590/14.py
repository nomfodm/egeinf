def f(n: str) -> str:
    while "2222" in n or "8888" in n:
        n = n.replace("2222", "88", 1)\
            .replace("8888", "22", 1)
            
    return n
    
print(f("8" * 70))

# 22
    