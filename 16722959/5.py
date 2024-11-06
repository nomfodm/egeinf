import time


a = sorted("АЛГОРИТМ")

counter = 0
for p1 in a:
    for p2 in a:
        for p3 in a:
            for p4 in a:
                s = p1 + p2 + p3 + p4
                counter += 1
                
                if s.startswith("ГО"):
                    print(counter)
                    exit(0)


