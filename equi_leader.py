def solution(A):
    leader, leader_count = find_Leader_with_count(A)
    if leader == -1:
        return 0
    equi_leaders_count = 0
    left_leaders_count = 0
    length = len(A)
    for i in range(length):
        if A[i] == leader:
            left_leaders_count += 1
        if left_leaders_count > (0.5) * (i + 1):
            right_leaders_count = leader_count - left_leaders_count
            if right_leaders_count > (0.5) * (length - i - 1):
                equi_leaders_count += 1
    
    return equi_leaders_count


def find_Leader_with_count(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader, count
