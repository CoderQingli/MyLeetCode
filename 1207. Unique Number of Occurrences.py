def uniqueOccurrences(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    dic = {}
    for a in arr:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    res = [dic[i] for i in dic]
    return len(res) == len(set(res))