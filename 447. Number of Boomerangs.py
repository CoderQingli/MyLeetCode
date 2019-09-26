def numberOfBoomerangs(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    l = len(points)
    res = 0
    for i in range(l):
        dic = {}
        for j in range(l):
            if i == j:
                continue
            d = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1
        for k in dic:
            if dic[k] > 1:
                res += dic[k] * (dic[k] - 1)
    return res