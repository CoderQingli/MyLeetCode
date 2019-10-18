def largestSumAfterKNegations(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    for i in range(K):
        A.sort()
        A[0] = -A[0]
    return sum(A)