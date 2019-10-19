def maxNumberOfBalloons(self, text):
    """
    :type text: str
    :rtype: int
    """
    res = []
    dic = {}
    for i in text:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if "b" in dic:
        res.append(dic["b"])
    else:
        return 0
    if "a" in dic:
        res.append(dic["a"])
    else:
        return 0
    if "l" in dic:
        tmp = dic["l"] // 2
        if tmp == 0:
            return 0
        else:
            res.append(tmp)
    else:
        return 0
    if "o" in dic:
        tmp = dic["o"] // 2
        if tmp == 0:
            return 0
        else:
            res.append(tmp)
    else:
        return 0
    if "n" in dic:
        res.append(dic["n"])
    else:
        return 0
    return min(res)