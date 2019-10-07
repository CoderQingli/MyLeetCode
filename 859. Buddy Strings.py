def buddyStrings(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    if len(A) != len(B):
        return False
    if A == B:
        return len(A) != len(set(A))
    tmp = []
    for a, b in zip(A, B):
        if a != b:
            tmp.append([a, b])
        if len(tmp) > 2:
            return False
    return len(tmp) == 2 and tmp[0] == tmp[1][::-1]