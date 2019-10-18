def duplicateZeros(self, arr):
    """
    :type arr: List[int]
    :rtype: None Do not return anything, modify arr in-place instead.
    """
    i = 0
    l = len(arr)
    while i < l:
        if arr[i] != 0:
            i += 1
        else:
            arr.insert(i + 1, 0)
            i += 2
            arr.pop()