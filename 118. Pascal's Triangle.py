def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1], [1, 1]]
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return res
    tmp = [1, 1]
    for i in range(2, numRows):
        cur = [1] * (i + 1)
        for j in range(1, len(cur) - 1):
            cur[j] = tmp[j - 1] + tmp[j]
        res.append(cur)
        tmp = cur
    return res