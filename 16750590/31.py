import os
filepath = os.path.join(os.path.dirname(__file__), "31.txt")

file = []
with open(filepath) as f:
    file.extend(map(int, f.readlines()))

max_element_ended_by_562 = max([i for i in file if str(i).endswith("562")])
    
def is_quadruple(a: int, b: int, c: int, d: int) -> bool:
    five_number_counter = 0
    non_five_number_counter = 0
    
    divisible_by_3 = 0
    divisible_by_7 = 0
    
    for i in map(str, [a, b, c, d]):
        if int(i) % 3 == 0:
            divisible_by_3 += 1
        if int(i) % 7 == 0:
            divisible_by_7 += 1
        
        if len(i) == 5:
            five_number_counter += 1
            continue
        non_five_number_counter += 1
        
    if five_number_counter < 1 or non_five_number_counter < 2:
        return False
    
    if divisible_by_7 < divisible_by_3:
        return False
    
    sum_ = sum([a, b, c, d])
    if sum_ > max_element_ended_by_562 and sum_ < max_element_ended_by_562 * 2:
        return True
    return False

quadruples = []
quadruples_sums = []

for i in range(3, len(file)):
    quadruple = [file[i], file[i - 1], file[i - 2], file[i - 3]]
    if is_quadruple(*quadruple):
        quadruples.append(quadruple)
        quadruples_sums.append(sum(quadruple))
        
print(len(quadruples))
print(max(quadruples_sums))
    
    
    
    