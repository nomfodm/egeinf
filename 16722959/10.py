def f(x: str) -> int:
    return int(f"28{x}2", 18) + int(f"93{x}5", 12)

digits = dict()
for i in range(10):
    digits[i] = str(i)
    
for i in range(ord("A"), ord("Z") + 1):
    digits[i - ord("A") + 10] = chr(i)
    
for x in range(12):
    g = f(digits[x])
    if g % 133 == 0:
        print(g // 133)
        break
    
    
    