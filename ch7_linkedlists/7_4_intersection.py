def intersection(L1,L2):
    def length(L):
        size = 0
        while L:
            L = L.next
            size += 1
        return size
    length1 = length(L1)
    length2 = length(L2)
    if length1 < length2:
        L2, L1 = L1, L2
        length1, length2 = length2, length1
    diff = length1 - length2
    for _ in range(diff):
        L1 = L1.next
    while L1 and L2:
        if L1 == L2:
            return True
        L1 = L1.next
        L2 = L2.next
    return False