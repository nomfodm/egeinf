def f(x: str):
    return int(f"3{x}DA", 14) + int(f"5{x}A6", 12)
    
digits = dict()
for i in range(10):
    digits[i] = str(i)
    
for i in range(ord("A"), ord("Z") + 1):
    digits[i - ord("A") + 10] = chr(i)
    
for x in range(0, 10):
    s = f(digits[x])
    if s % 81 == 0:
        print(s // 81)
        exit(0)
    
# 250
