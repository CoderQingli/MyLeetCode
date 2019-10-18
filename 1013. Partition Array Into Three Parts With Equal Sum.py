def canThreePartsEqualSum(self, A):
    """
    :type A: List[int]
    :rtype: bool
    """
    s = sum(A)
    if s % 3 != 0:
        return False
    tmp = 0
    flag = 0
    for a in A:
        tmp += a
        if tmp == s / 3:
            if flag == 1:
                return True
            tmp = 0
            flag = 1
    return False