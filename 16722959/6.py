a = "0123456789"
b = "123456789"


ans = []
for p1 in b:
    for p2 in a:
        for p3 in a:
            for p4 in a:
                s = p1 + p2 + p3 + p4
                
                if len(set(s)) != len(s):
                    continue
                
                s = s.replace("2", "0")\
                    .replace("4", "0")\
                    .replace("6", "0")\
                    .replace("8", "0")
                
                s = s.replace("3", "1")\
                    .replace("5", "1")\
                    .replace("7", "1")\
                    .replace("9", "1")
                    
                if "11" in s or "00" in s:
                    continue
                
                ans.append(s)
                
print(len(ans))    
                
                
                
                