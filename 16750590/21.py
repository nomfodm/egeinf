P = range(69, 91 + 1)
Q = range(77, 114 + 1)

def f(x: int, A: range):
    global P, Q
    return (x in Q) <= (((x in P) == (x in Q)) or ((x not in P) <= (x in A)))


ranges = []
for Amin in range(1, 200):
    for Amax in range(Amin + 1, 200):
        A = range(Amin, Amax)
        
        flag = False
        for x in range(-500, 500):
            if not f(x, A):
                flag = True
                
        if flag:
            continue
        
        ranges.append(len(A))
        
print(min(ranges))

# 23
