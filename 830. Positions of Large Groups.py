def largeGroupPositions(self, S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    res = []
    i = 0
    for j in range(len(S)):
        if j == len(S) - 1 or S[j] != S[j + 1]:
            if j - i + 1 >= 3:
                res.append([i, j])
            i = j + 1
    return res