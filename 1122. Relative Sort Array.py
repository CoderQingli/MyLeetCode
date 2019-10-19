def relativeSortArray(self, arr1, arr2):
    """
    :type arr1: List[int]
    :type arr2: List[int]
    :rtype: List[int]
    """
    tmp = []
    dic = {}
    res = []
    for i in arr1:
        if i in dic:
            dic[i] += 1
        elif i in arr2:
            dic[i] = 1
        else:
            tmp.append(i)
    for j in arr2:
        res.extend([j] * dic[j])
    tmp.sort()
    return res + tmp