def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    n = len(A)
    j = 0
    while j < n and A[j] < 0:
        j += 1
    i = j - 1

    res = []
    while i >= 0 and j < n:
        if A[i] ** 2 < A[j] ** 2:
            res.append(A[i] ** 2)
            i -= 1
        else:
            res.append(A[j] ** 2)
            j += 1
    while i >= 0:
        res.append(A[i] ** 2)
        i -= 1
    while j < n:
        res.append(A[j] ** 2)
        j += 1
    return res