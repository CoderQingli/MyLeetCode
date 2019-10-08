def isMonotonic(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    inc = dec = True
    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            dec = False
        if A[i] > A[i + 1]:
            inc = False
    return inc or dec