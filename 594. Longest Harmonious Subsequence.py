def findLHS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dic = {}
    for n in nums:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    res = 0
    for i in dic:
        if i + 1 in dic:
            if dic[i] + dic[i + 1] > res:
                res = dic[i] + dic[i + 1]
    return res