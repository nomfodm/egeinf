P = range(4, 15)
Q = range(12, 20)

def f(x: int, A: range):
    global P, Q
    return ((x in P) and (x in Q)) <= (x in A)


answer = []
for Amin in range(1, 50):
    for Amax in range(Amin + 1, 50):
        counter = 0
        A = range(Amin, Amax)
        for x in range(-500, 500):
            if f(x, A):
                counter += 1
                
        if counter != 1000:
            continue
        
        answer.append(len(A))
        
print(min(answer))

