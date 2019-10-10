def validMountainArray(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    if len(A) < 3:
        return False
    flag = 0
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return False
        if flag == 0:
            if A[i] > A[i + 1]:
                flag = 1
                continue
        if flag == 1:
            if A[i] < A[i + 1]:
                return False
    return flag == 1 and A[0] < A[1]