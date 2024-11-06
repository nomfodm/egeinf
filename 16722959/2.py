from itertools import permutations, product


def f(x, y, z, w):
    return ((w <= (not x)) == (z <= y)) and (y or w)


for x1, x2 in product([1, 0], repeat=2):
    table = [
        (1, 1, 1, 0),
        (0, 0, 1, 1),
        (0, x1, 0, x2)
    ]
    
    if len(set(table)) != len(table):
        continue
    
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [0, 1, 1]:
            print(*p)
    


