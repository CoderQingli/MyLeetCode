def findMaxConsecutiveOnes(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    l = [str(n) for n in nums]
    l = "".join(l).replace("0", " ").split(" ")
    res = 0
    for i in l:
        res = max(res, len(i))
    return res