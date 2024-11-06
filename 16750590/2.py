from itertools import permutations, product


def f(x, y, z, w):
    return ((not x) or (not y)) and (not (x == z)) and w


for x1, x2, x3 in product([1, 0], repeat=3):
    table = [
        (1, x1, 0, 0),
        (1, 0, 0, 1),
        (1, 0, x2, x3)
    ]
    
    if len(table) != len(set(table)):
        continue
    
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
            
# wxyz
