def f(n: int):
    n_str = str(n)
    triples = []
    for i in range(len(n_str) - 1, 2 - 1, -1):
        triple = n_str[i] + n_str[i - 1] + n_str[i - 2]
        triples.append(int(triple[::-1]))
        
    r = max(triples) - min(triples)
    if r == 415:
        print(n)
        exit(0)
    
for n in range(100, 5000):
    f(n)
    
# 1572
