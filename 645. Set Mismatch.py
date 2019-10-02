def findErrorNums(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dic = {}
    n = len(nums)
    res = [0, 0]
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in range(1, n + 1):
        if i not in dic:
            res[1] = i
        elif dic[i] == 2:
            res[0] = i
    return res