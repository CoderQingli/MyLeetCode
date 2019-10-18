def removeDuplicates(self, S):
    """
    :type S: str
    :rtype: str
    """
    res = []
    for i in range(len(S)):
        if res and res[-1] == S[i]:
            res.pop()
        else:
            res.append(S[i])
    return "".join(res)