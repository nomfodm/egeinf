from itertools import permutations, product


def f(x, y, z, w):
    return ((x <= y) == (z <= w)) or (x and w)


for x1, x2, x3, x4, x5, x6 in product([1, 0], repeat=6):
    table = [
        (1, x1, x2, x3),
        (1, 1, x4, x5),
        (1, 1, 1, x6)
    ]
    
    if len(set(table)) != len(table):
        continue
    
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]:
            print(*p)
    


