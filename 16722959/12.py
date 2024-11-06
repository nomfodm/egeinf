def f(x: int, A: int):
    return ((x & 25) != 0) <= (((x & 17) == 0) <= ((x & A) != 0))


for A in range(0, 500):
    counter = 0
    for x in range(0, 500):
        if f(x, A):
            counter += 1
            
    if counter != 500:
        continue
    
    print(A)
    break    
    