a = "БРОНХИ"

answer = 0
for p1 in a:
    for p2 in a:
        for p3 in a:
            for p4 in a:
                s = p1 + p2 + p3 + p4
                
                if s.count("Х") != 1:
                    continue
                
                answer += 1
                
print(answer)
                
# 500
