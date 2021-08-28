from typing import List

def second_max(n: int, A: List[int]):
    return sorted(A)[-2]


t1 = second_max(7, [1,4,6,7,3,4,6])
print(t1)
