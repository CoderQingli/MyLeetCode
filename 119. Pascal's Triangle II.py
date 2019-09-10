def getRow(self, rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    res = [[1], [1, 1]]
    if rowIndex == 0 or rowIndex == 1:
        return res[rowIndex]
    tmp = [1, 1]
    for i in range(2, rowIndex + 1):
        cur = [1] * (i + 1)
        for j in range(1, len(cur) - 1):
            cur[j] = tmp[j - 1] + tmp[j]
        res.append(cur)
        tmp = cur
    return res[rowIndex]