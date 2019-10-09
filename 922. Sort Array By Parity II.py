def sortArrayByParityII(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    for i in range(len(A)):
        if i % 2 == 0:
            A[i] = even.pop()
        else:
            A[i] = odd.pop()
    return A