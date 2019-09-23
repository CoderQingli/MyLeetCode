def thirdMax(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = []
    for n in nums:
        if n in res:
            continue
        if len(res) < 3:
            res.append(n)
            res.sort()
            continue
        if n > res[0]:
            res[0] = n
            res.sort()
    if len(set(res)) == 3:
        return res[0]
    else:
        return max(nums)