from itertools import permutations, product


def f(w, x, y, z):
    return ((x or y) <= (y and w)) == (not ((y and z) <= (w or x)))


for x1, x2 in product([1, 0], repeat=2):
    table = [
        (1, 1, x1, 1),
        (0, x2, 0, 0),
        (0, 0, 1, 1)
    ]
    
    if len(table) != len(set(table)):
        continue
    
    for p in permutations("wxyz"):
        if [f(**dict(zip(p, t))) for t in table] == [1, 1, 1]:
            print("".join(p))
            
# zywx
            