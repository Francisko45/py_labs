import random
U = set(range(1, 26))
A = set(random.sample(list(U), 12))
B = set(random.sample(list(U), 14))
C = set(random.sample(list(U), 9))
union = A | B
comp = U - union
compA = U - A
compB = U - C
compC = compA & compB
result_set = compC - compB
element = sorted(result_set)
result = len(result_set)
print("Множина A:", sorted(A))
print("Множина B:", sorted(B))
print("Множина C:", sorted(C))
print("Результуюча множина:", element)
print("Потужність результуючої множини:", result)
