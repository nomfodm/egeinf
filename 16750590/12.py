a = "ПАРАБОЛА"


answer = 0
for p1 in a:
    for p2 in a:
        for p3 in a:
            for p4 in a:
                for p5 in a:
                    for p6 in a:
                        for p7 in a:
                            for p8 in a:
                                s = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
                                
                                if s.count("А") != 3 or\
                                    s.count("П") != 1 or \
                                    s.count("Р") != 1 or \
                                    s.count("Б") != 1 or \
                                    s.count("Л") != 1:
                                        continue
                                    
                                if "АА" in s or "ОА" in s or "АО" in s:
                                    continue
                                
                                if "ПР" in s or "РП" in s or "РБ" in s or "БР" in s or "БЛ" in s or "ЛБ" in s:
                                    continue
                                
                                answer += 1
                                
print(answer)

# 9072
