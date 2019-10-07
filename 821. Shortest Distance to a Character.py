def shortestToChar(self, S, C):
    """
    :type S: str
    :type C: str
    :rtype: List[int]
    """
    tmp = float("-inf")
    ans = []
    for i, x in enumerate(S):
        if x == C:
            tmp = i
        ans.append(i - tmp)

    tmp = float("inf")
    for i in xrange(len(S) - 1, -1, -1):
        if S[i] == C:
            tmp = i
        ans[i] = min(ans[i], tmp - i)

    return ans