def addToArrayForm(self, A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: List[int]
    """
    a = int("".join(map(str, A)))
    res = a + K
    return list(str(res))