def missingNumber(self, arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    gap = (arr[-1] - arr[0]) / len(arr)
    if gap == 0:
        return arr[0]
    tmp = arr[0]
    for a in arr:
        if a != tmp:
            return tmp
        else:
            tmp += gap