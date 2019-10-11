def sumEvenAfterQueries(self, A, queries):
    """
    :type A: List[int]
    :type queries: List[List[int]]
    :rtype: List[int]
    """
    s = sum(x for x in A if x % 2 == 0)
    res = []

    for x, k in queries:
        if A[k] % 2 == 0:
            s -= A[k]
        A[k] += x
        if A[k] % 2 == 0:
            s += A[k]
        res.append(s)
    return res