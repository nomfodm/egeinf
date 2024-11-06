def f(n: str) -> str:
    while "10" in n or "1" in n:
        if "10" in n:
            n = n.replace("10", "001", 1)
        elif "1" in n:
            n = n.replace("1", "000", 1)
            
    return n


s = "1" + "0" * 80
g = f(s)
print(g.count("0"))
    
    
    
    