import os
filepath = os.path.join(os.path.dirname(__file__), "29.txt")

file = []
with open(filepath) as f:
    file.extend(map(int, f.readlines()))

max_element_ended_by_15 = max([i for i in file if str(i).endswith("15")])

def is_triple(a: int, b: int, c: int) -> bool:
    four_number_counter = 0
    for i in map(str, [a, b, c]):
        if len(i) == 4:
            four_number_counter += 1
    
    if four_number_counter != 1:
        return False
    
    if sum([a, b, c]) < max_element_ended_by_15:
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

# 299
# 196183
