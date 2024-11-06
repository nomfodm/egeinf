import os
filepath = os.path.join(os.path.dirname(__file__), "30.txt")

file = []
with open(filepath) as f:
    file.extend(map(int, f.readlines()))
     
max_element_ended_by_29 = max([i for i in file if str(i).endswith("29")])

def is_triple(a: int, b: int, c: int) -> bool:
    five_number_counter = 0
    for i in map(str, map(abs, [a, b, c])):
        if len(i) == 5:
            five_number_counter += 1
            
    if five_number_counter != 2:
        return False
    
    if sum([a, b, c]) > max_element_ended_by_29:
        return False
    return True

triples = []
triples_sums = []

for i in range(2, len(file)):
    triple = [file[i], file[i - 1], file[i - 2]]
    if is_triple(*triple):
        triples.append(triple)
        triples_sums.append(sum(triple))

print(len(triples))
print(max(triples_sums))

# 157
# 973622
