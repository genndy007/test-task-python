from typing import List

def second_max(n: int, A: List[int]):
    return sorted(A)[-2]


def second_max_myself(A: List[int]) -> int:
    if len(A) < 2:
        raise Exception('Cannot find second in such little array')

    (cur_max, cur_second) = (A[0], A[1]) if A[0] > A[1] else (A[1], A[0])

    for unit in A:
        if unit > cur_max:
            cur_second = cur_max
            cur_max = unit

    return cur_second




# t1 = second_max(7, [1,4,6,7,3,4,6])
# print(t1)


t2 = second_max_myself([1,4,6,7,3,4,6])
print(t2)
