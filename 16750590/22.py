def f(x: int, y: int, A: int):
    return (2 * x + 3 * y < A) or (x > y) or (y > 24)


for A in range(0, 300):
    counter = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if f(x, y, A):
                counter += 1
    
    if counter != 300 * 300:
        continue
    
    print(A)
    break

# 121
