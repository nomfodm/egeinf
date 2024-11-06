from itertools import permutations, product


def f(w, x, y, z):
    return (x or (not y)) and (not (y == z)) and (not w)


for x1, x2, x3, x4 in product([1, 0], repeat=4):
    table = [
        (1, 1, x1, x2),
        (x3, 1, 0, 0),
        (1, x4, 1, 0)
    ]
    
    if len(table) != len(set(table)):
        continue
    
    for p in permutations("wxyz"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
            
# xzyw
