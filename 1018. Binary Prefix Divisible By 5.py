def prefixesDivBy5(self, A):
    """
    :type A: List[int]
    :rtype: List[bool]
    """
    res = [A[0] % 5 == 0]
    s = A[0]
    for i in range(1, len(A)):
        s = s * 2 + A[i]
        if s % 5 == 0:
            res.append(True)
        else:
            res.append(False)
    return res