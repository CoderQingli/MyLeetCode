def findJudge(self, N, trust):
    """
    :type N: int
    :type trust: List[List[int]]
    :rtype: int
    """
    n = [i for i in range(1, N + 1)]
    for p in trust:
        if p[0] in n:
            n.remove(p[0])
    if len(n) == 0:
        return -1
    for j in n:
        cnt = 0
        for k in trust:
            if k[1] == j:
                cnt += 1
        if cnt == N - 1:
            return j
    return -1