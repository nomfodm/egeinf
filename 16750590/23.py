def dl(x, y):
    return x % y == 0

def f(x, A):
    return dl(x, A) or ((x in range(70, 90 + 1)) <= (not dl(x, 22)))

for A in range(300, 0, -1):
    flag = False
    for x in range(1, 300):
        if not f(x, A):
            flag = True
            
    if flag:
        continue
    
    print(A)
    break

# 88
