def f(x: int, A: int):
    return ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & A != 0))

for A in range(0, 300):
    flag = False
    for x in range(0, 300):
        if not f(x, A):
            flag = True
            
    if flag:
        continue
    
    print(A)
    break

# 33
