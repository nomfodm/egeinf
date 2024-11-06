a = "КОНФЕТА"
b = "КОНЕТА"

answer = 0
for p1 in a:
    for p2 in b:
        for p3 in a:
            for p4 in a:
                for p5 in a:
                    s = p1 + p2 + p3 + p4 + p5
                    
                    if s.count("Е") != 2:
                        continue
                    
                    answer += 1
                    
print(answer)           
                    
# 1944
