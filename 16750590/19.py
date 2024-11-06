def f(x: str, y: str):
    return int(f"2{y}66{x}", 9) + int(f"{x}9{y}1", 12)

digits = dict()
for i in range(10):
    digits[i] = str(i)
    
for i in range(ord("A"), ord("Z") + 1):
    digits[i - ord("A") + 10] = chr(i)
    
for x in range(0, 9):
    for y in range(0, 9):
        s = f(digits[x], digits[y])
        if s % 170 == 0:
            print(s // 170)

# 165
