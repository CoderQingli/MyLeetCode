def minimumAbsDifference(self, arr):
    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    a = sorted(arr)
    dic = {}
    for i in range(len(a) - 1):
        if abs(a[i] - a[i + 1]) in dic:
            dic[abs(a[i] - a[i + 1])].append([a[i], a[i + 1]])
        else:
            dic[abs(a[i] - a[i + 1])] = [[a[i], a[i + 1]]]
    return dic[min(dic)]