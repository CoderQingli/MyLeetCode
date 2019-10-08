def fairCandySwap(self, A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    sa = sum(A)
    sb = sum(B)
    s = set(B)
    tmp = (sb - sa) / 2
    for a in A:
        if a + tmp in s:
            return [a, a + tmp]