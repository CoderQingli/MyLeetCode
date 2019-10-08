def uncommonFromSentences(self, A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    res = []
    tmp = A.split() + B.split()
    for word in tmp:
        if tmp.count(word) == 1:
            res.append(word)
    return res