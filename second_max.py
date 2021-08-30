from typing import List

def second_max(n: int, A: List[int]):
    return sorted(A)[-2]


def second_max_myself(A: List[int]) -> int:
    if len(A) < 2:
        raise Exception('Cannot find second in such little array')

    cur_max = cur_second = -float('inf')

    for i in range(len(A)):
        if A[i] > cur_max:
            cur_second = cur_max
            cur_max = A[i]
        elif A[i] > cur_second:
            cur_second = A[i]

    return cur_second




# t1 = second_max(7, [1,4,6,7,3,4,6])
# print(t1)


# t2 = second_max_myself([1,4,6,7,3,4,6])
# print(t2)

tests = [
    [1, 2],
    [4, 5, 6, 7, 18, 2],
    [5, 5, 5, 5],
    [17, 3, 2, 1],
    [17, 17, 1],
    [1, 1, 17]
]

for test in tests:
    print(test, second_max_myself(test))