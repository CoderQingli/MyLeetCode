def sortArrayByParity(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    i, j = 0, len(A) - 1
    while i < j:
        if A[i] % 2 != 0 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        if A[i] % 2 == 0:
            i += 1
        if A[j] % 2 != 0:
            j -= 1
    return A